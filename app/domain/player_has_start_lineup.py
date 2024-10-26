from __future__ import annotations
from typing import Dict, Any
from app import db


class PlayerHasStartLineup(db.Model):
    __tablename__ = 'player_has_start_lineup'
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    start_lineup_id = db.Column(db.Integer, db.ForeignKey('start_lineup.id'), nullable=False)

    def __repr__(self) -> str:
        return f"PlayerHasStartLineup(player_id='{self.player_id}', start_lineup_id='{self.start_lineup_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'player_id': self.player_id,
            'start_lineup_id': self.start_lineup_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PlayerHasStartLineup:
        player_has_start_lineup = PlayerHasStartLineup(
            player_id=dto_dict.get('player_id'),
            start_lineup_id=dto_dict.get('start_lineup_id'),
        )
        return player_has_start_lineup
