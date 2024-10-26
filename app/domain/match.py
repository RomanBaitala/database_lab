from __future__ import annotations
from typing import Dict, Any
from app import db


class FMatch(db.Model):
    __tablename__ = 'fmatch'
    id = db.Column(db.Integer, primary_key=True)
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team_league_id = db.Column(db.Integer, db.ForeignKey('league.id'), nullable=False)
    referee_team_id = db.Column(db.Integer, db.ForeignKey('referee_team.id'), nullable=False)
    stadium_id = db.Column(db.Integer, db.ForeignKey('stadium.id'), nullable=False)
    home_start_lineup = db.Column(db.Integer, db.ForeignKey('start_lineup.id'), nullable=False)
    away_start_lineup = db.Column(db.Integer, db.ForeignKey('start_lineup.id'), nullable=False)

    def __repr__(self) -> str:
        return f"FMatch(id='{self.id}', home_team_id={self.home_team_id}, away_team_id='{self.away_team_id}', " \
               f"team_league_id='{self.team_league_id}', referee_team_id={self.referee_team_id}, " \
               f"stadium_id={self.stadium_id}, home_start_lineup='{self.home_start_lineup}," \
               f"away_start_lineup='{self.away_start_lineup}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'home_team_id': self.home_team_id,
            'away_team_id': self.away_team_id,
            'team_league_id': self.team_league_id,
            'referee_team_id': self.referee_team_id,
            'stadium_id': self.stadium_id,
            'home_start_lineup': self.home_start_lineup,
            'away_start_lineup': self.away_start_lineup
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> FMatch:
        fmatch = FMatch(
            home_team_id=dto_dict.get('home_team_id'),
            away_team_id=dto_dict.get('away_team_id'),
            team_league_id=dto_dict.get('team_league_id'),
            referee_team_id=dto_dict.get('referee_team_id'),
            stadium_id=dto_dict.get('stadium_id'),
            home_start_lineup=dto_dict.get('home_start_lineup'),
            away_start_lineup=dto_dict.get('away_start_lineup')
        )
        return fmatch
