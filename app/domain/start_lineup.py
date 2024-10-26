from __future__ import annotations
from typing import Dict, Any
from app import db


class StartLineup(db.Model):
    __tablename__ = 'start_lineup'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    start_players = db.relationship('Player',
                                    secondary='player_has_start_lineup',
                                    back_populates='player_start_lineup')

    def __repr__(self) -> str:
        return f"StartLineup(id='{self.id}', , team_id=={self.team_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        start_players = [start_player.put_into_dto() for start_player in self.start_players]
        return {
            'id': self.id,
            'team_id': self.team_id,
            'start_players': start_players if start_players else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> StartLineup:
        start_lineup = StartLineup(
            team_id=dto_dict.get('team_id'),
        )
        return start_lineup
