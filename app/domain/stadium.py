from __future__ import annotations
from typing import Dict, Any
from app import db
from ..connection import create_connection


class Stadium(db.Model):
    __tablename__ = 'stadium'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"Stadium(id='{self.id}', name='{self.name}', capacity='{self.capacity}', location='{self.location}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'capacity': self.capacity,
            'location': self.location,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Stadium:
        stadium = Stadium(
            name=dto_dict.get('name'),
            capacity=dto_dict.get('capacity'),
            location=dto_dict.get('location'),
        )
        return stadium


def get_through_capacity(stat_type):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.callproc('info_about_capacity', (stat_type,))
        connection.commit()
        cursor.execute("SELECT @result;")
        return cursor.fetchone()[0]

    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()
