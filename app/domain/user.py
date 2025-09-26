from __future__ import annotations
from typing import Dict, Any
from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self) -> str:
        return f"User(id='{self.id}', username='{self.username}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'username': self.username,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        return User(
            username=dto_dict.get('username'),
            password=dto_dict.get('password'),
        )
