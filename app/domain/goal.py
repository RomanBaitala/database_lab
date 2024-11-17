from __future__ import annotations
from typing import Dict, Any
from app import db


class Goal(db.Model):
    __tablename__ = 'goal'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Float, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    player_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('fmatch.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Goal(id={self.id}, time='{self.time}', player_id={self.player_id}, " \
               f"player_team_id={self.player_team_id}, match_id='{self.match_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'time': self.time,
            'player_id': self.player_id,
            'player_team_id': self.player_team_id,
            'match_id': self.match_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Goal:
        goal = Goal(
            player_team_id=dto_dict.get('player_team_id'),
            time=dto_dict.get('time'),
            player_id=dto_dict.get('player_id'),
            match_id=dto_dict.get('match_id'),
        )
        return goal


def insert_goal(time: float, player_id: int, player_team_id: int, match_id: int) -> Goal:
    new_goal = Goal(time=time, player_id=player_id, player_team_id=player_team_id, match_id=match_id)
    db.session.add(new_goal)
    db.session.commit()
    return new_goal
