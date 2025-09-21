import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api
from flasgger import Swagger
from app.config import Config
from app.root import register_routes
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    swagger = Swagger(app)

    db.init_app(app)
    register_routes(app)
    create_database()
    create_tables(app)
    populate_data()
    return app


def create_database():
    connection = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "127.0.0.1"),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', 'root'),
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.environ.get('DB_NAME', 'footballdb')}")
    cursor.close()
    connection.close()


def create_tables(app):
    with app.app_context():
        db.create_all()


def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists('data.sql'):
        connection = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "127.0.0.1"),
            user=os.environ.get('DB_USER', 'root'),
            password=os.environ.get('DB_PASSWORD', 'root'),
            database=os.environ.get('DB_NAME', 'footballdb')
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
