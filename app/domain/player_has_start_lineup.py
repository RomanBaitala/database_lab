from __future__ import annotations
from typing import Dict, Any
from app import db
from .player import Player
from .start_lineup import StartLineup
from ..connection import create_connection


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


def add_player_to_start_lineup(p_player_name: str, p_player_surname: str, p_lineup_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.callproc('many_to_many_relation', (p_player_name, p_player_surname, p_lineup_id))
        connection.commit()

        # return new_start_lineup
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()
