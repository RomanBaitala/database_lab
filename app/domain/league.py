from __future__ import annotations
from typing import Dict, Any
from app import db


class League(db.Model):
    __tablename__ = 'league'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    team_count = db.Column(db.Integer, nullable=False)
    teams = db.relationship('Team', backref='league')

    def __repr__(self) -> str:
        return f"HotelChain({self.id}, 'name={self.name}', team_count='{self.team_count}')"

    def put_into_dto(self) -> Dict[str, Any]:
        teams = [team.put_into_dto() for team in self.teams]
        return {
            'id': self.id,
            'name': self.name,
            'team_count': self.team_count,
            'teams': teams if teams else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> League:
        league = League(
            name=dto_dict.get('name'),
            team_count=dto_dict.get('team_count'),
        )
        return league
