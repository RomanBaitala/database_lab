from __future__ import annotations
from typing import Dict, Any
from app import db


class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    nationality = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    # team_league_id = db.Column(db.Integer, db.ForeignKey('team.league_id'), nullable=False)

    player_start_lineup = db.relationship('StartLineup',
                                          secondary='player_has_start_lineup',
                                          back_populates='start_players')

    def __repr__(self) -> str:
        return f"Player(id={self.id}, name={self.name}, surname={self.surname}, " \
               f"nationality={self.nationality}, age='{self.age}', " \
               f"team_id={self.team_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'nationality': self.nationality,
            'age': self.age,
            'team_id': self.team_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Player:
        player = Player(
            name=dto_dict.get('name'),
            surname=dto_dict.get('surname'),
            nationality=dto_dict.get('nationality'),
            age=dto_dict.get('age'),
            team_id=dto_dict.get('team_id'),
        )
        return player
