from __future__ import annotations
from typing import Dict, Any
from app import db


class PlayerStat(db.Model):
    __tablename__ = 'player_stat'
    id = db.Column(db.Integer, primary_key=True)
    scored = db.Column(db.Integer, nullable=False)
    games_mark = db.Column(db.Float, nullable=False)
    games_played = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

    def __repr__(self) -> str:
        return (f"PlayerStat({self.id}, scored='{self.scored}', games_mark='{self.games_mark}',"
                f" games_played='{self.games_played}', player_id='{self.player_id}')")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'scored': self.scored,
            'games_mark': self.games_mark,
            'games_played': self.games_played,
            'player_id': self.player_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PlayerStat:
        player_stat = PlayerStat(
            name=dto_dict.get('name'),
            address=dto_dict.get('address'),
            contact_info=dto_dict.get('contact_info'),
            rating=dto_dict.get('rating'),
            HotelChain_id=dto_dict.get('HotelChain_id')
        )
        return player_stat
