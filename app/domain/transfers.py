from __future__ import annotations
from typing import Dict, Any
from app import db
from sqlalchemy import event, select


class Transfer(db.Model):
    __tablename__ = 'transfers'
    id = db.Column(db.Integer, primary_key=True)
    team_from = db.Column(db.Integer, nullable=False)
    team_to = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return f"Transfer(id='{self.id}', team_from={self.team_from}, team_to={self.team_to}, " \
               f"player_id={self.player_id}, value={self.value}, date={self.date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'team_from': self.team_from,
            'team_to': self.team_to,
            'player_id': self.player_id,
            'value': self.value,
            'date': self.date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Transfer:
        transfer = Transfer(
            team_from=dto_dict.get('team_from'),
            team_to=dto_dict.get('team_to'),
            player_id=dto_dict.get('player_id'),
            value=dto_dict.get('value'),
            date=dto_dict.get('date')
        )
        return transfer
