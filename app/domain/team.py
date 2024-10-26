from __future__ import annotations
from typing import Dict, Any
from app import db


class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    coach = db.Column(db.String(65), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), nullable=False)
    stadium_id = db.Column(db.Integer, db.ForeignKey('stadium.id'), nullable=False)
    players = db.relationship('Player', backref='team')
    matches_home = db.relationship('FMatch', foreign_keys='FMatch.home_team_id')

    def __repr__(self) -> str:
        return (f"Team(id='{self.id}', name='{self.name}', coach='{self.coach}', league_id='{self.league_id}', "
                f"stadium_id='{self.stadium_id}')")

    def put_into_dto(self) -> Dict[str, Any]:
        players = [player.put_into_dto() for player in self.players]
        matches = [match.put_into_dto() for match in self.matches_home]
        return {
            'id': self.id,
            'name': self.name,
            'coach': self.coach,
            'league_id': self.league_id,
            'stadium_id': self.stadium_id,
            'players': players if players else None,
            'matches': matches if matches else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Team:
        team = Team(
            name=dto_dict.get('name'),
            coach=dto_dict.get('coach'),
            league_id=dto_dict.get('league_id'),
            stadium_id=dto_dict.get('stadium_id'),
        )
        return team
