from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import User
from werkzeug.security import generate_password_hash

auth_blueprint = Blueprint("auth", __name__)
db = SQLAlchemy()


@auth_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        # Assuming `generate_token` is a method on your User model
        token = user.generate_token()
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401


@auth_blueprint.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    new_user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return (
        jsonify({"message": "User created successfully", "user_id": new_user.id}),
        201,
    )
