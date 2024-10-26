from __future__ import annotations
from typing import Dict, Any
from app import db


class Referee(db.Model):
    __tablename__ = 'referee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(40), nullable=False)

    referee_team = db.relationship('RefereeTeam',
                                   secondary='referee_has_referee_team',
                                   back_populates='referees')

    def __repr__(self) -> str:
        return f"Referee(id={self.id}, name='{self.name}', surname='{self.surname}', age='{self.age}', " \
               f"gender={self.gender}, position='{self.position}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'gender': self.gender,
            'position': self.position,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Referee:
        referee = Referee(
            name=dto_dict.get('name'),
            surname=dto_dict.get('surname'),
            age=dto_dict.get('age'),
            gender=dto_dict.get('gender'),
            position=dto_dict.get('position'),
        )
        return referee
