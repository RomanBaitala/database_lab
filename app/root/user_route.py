from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from passlib.hash import pbkdf2_sha256

from .. import db
from ..domain import User
from blocklist import BLOCKLIST

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/login", methods=["POST"])
def login():
    """
       User login
       ---
       tags:
         - Authentication
       parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - username
                - password
              properties:
                username:
                  type: string
                  example: newuser
                password:
                  type: string
                  example: mypassword
       requestBody:
         required: true
         content:
           application/json:
             schema:
               type: object
               required:
                 - username
                 - password
               properties:
                 username:
                   type: string
                   example: johndoe
                 password:
                   type: string
                   example: secret123
       responses:
         200:
           description: Successful login, JWT access token returned
           content:
             application/json:
               schema:
                 type: object
                 properties:
                   access_token:
                     type: string
                     example: eyJhbGciOiJIUzI1NiIsInR5cCI...
         400:
           description: Missing username or password
         401:
           description: Incorrect username or password
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = User.query.filter_by(username=username).first()
    if user and pbkdf2_sha256.verify(password, user.password):
        access_token = create_access_token(identity=str(user.id))
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Incorrect username or password"}), 401


@user_bp.route("/register", methods=["POST"])
def register():
    """
       User registration
       ---
       tags:
         - Authentication
       parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - username
                - password
              properties:
                username:
                  type: string
                  example: newuser
                password:
                  type: string
                  example: mypassword
       requestBody:
         required: true
         content:
           application/json:
             schema:
               type: object
               required:
                 - username
                 - password
               properties:
                 username:
                   type: string
                   example: newuser
                 password:
                   type: string
                   example: mypassword
       responses:
         201:
           description: User created successfully
           content:
             application/json:
               schema:
                 type: object
                 properties:
                   message:
                     type: string
                     example: User created successfully
         400:
           description: Username or password missing
         409:
           description: User already exists
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 409

    user = User(
        username=username,
        password=pbkdf2_sha256.hash(password),
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201


@user_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """
        User logout
        ---
        tags:
          - Authentication
        security:
          - bearerAuth: []
        responses:
          200:
            description: Successfully logged out
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
                      example: Successfully logged out
    """
    jti = get_jwt()["jti"]
    BLOCKLIST.add(jti)
    return jsonify({"message": "Successfully logged out"}), 200
