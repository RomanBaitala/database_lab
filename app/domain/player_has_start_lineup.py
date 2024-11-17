from __future__ import annotations
from typing import Dict, Any
from app import db
from .player import Player
from .start_lineup import StartLineup


class PlayerHasStartLineup(db.Model):
    __tablename__ = 'player_has_start_lineup'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    start_lineup_id = db.Column(db.Integer, db.ForeignKey('start_lineup.id'), nullable=False)

    def __repr__(self) -> str:
        return f"PlayerHasStartLineup(id='{self.id}', player_id='{self.player_id}', start_lineup_id='{self.start_lineup_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
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

    @staticmethod
    def add_player_to_start_lineup(player_name: str, player_surname: str, lineup_id: int) -> PlayerHasStartLineup:
        player = Player.query.filter_by(name=player_name, surname=player_surname).first()
        if not player:
            raise ValueError("Player not found")

        lineup = StartLineup.query.get(lineup_id)
        if not lineup:
            raise ValueError("Start lineup not found")

        player_has_start_lineup = PlayerHasStartLineup(player_id=player.id, start_lineup_id=lineup.id)
        db.session.add(player_has_start_lineup)
        db.session.commit()
        return player_has_start_lineup


