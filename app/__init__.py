import mysql.connector
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST
from flasgger import Swagger
from app.config import Config
from app.root import register_routes
import os
from dotenv import load_dotenv

load_dotenv()
jwt = JWTManager()

swagger_template = {
    "swagger": "2.0",   # Flasgger defaults to Swagger 2.0, not OpenAPI 3.0
    "info": {
        "title": "My API",
        "description": "API documentation for football website",
        "version": "1.0.0",
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
        }
    },
    "security": [
        {
            "Bearer": []
        }
    ]
}

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {"description": "The token has been revoked.", "error": "token_revoked"}
        ),
        401,
    )

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JWT_SECRET_KEY'] =  os.environ.get('JWT_SECRET_KEY')
    swagger = Swagger(app, template=swagger_template)

    db.init_app(app)
    jwt.init_app(app)
    register_routes(app)
    create_database()
    create_tables(app)
    populate_data()
    return app


def create_database():
    connection = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.environ.get('DB_NAME')}")
    cursor.close()
    connection.close()


def create_tables(app):
    with app.app_context():
        db.create_all()


def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists('data.sql'):
        connection = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            database=os.environ.get('DB_NAME')
        )
        cursor = connection.cursor()
        with open(sql_file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:

                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except mysql.connector.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        connection.rollback()
        cursor.close()
        connection.close()
