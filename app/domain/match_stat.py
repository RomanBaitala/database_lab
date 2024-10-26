from __future__ import annotations
from typing import Dict, Any
from app import db


class MatchStat(db.Model):
    __tablename__ = 'match_stat'
    match_id = db.Column(db.Integer, db.ForeignKey('fmatch.id'), primary_key=True)
    yellow_card = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Integer, nullable=False)
    red_card = db.Column(db.Integer, nullable=False)
    possession = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"MatchStat(match_id={self.match_id}, yellow_card={self.yellow_card}, red_card={self.red_card}, " \
               f"possession='{self.possession}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'match_id': self.match_id,
            'yellow_card': self.yellow_card,
            'goals': self.goals,
            'red_card': self.red_card,
            'possession': self.possession
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MatchStat:
        match_stat = MatchStat(
            yellow_card=dto_dict.get('yellow_card'),
            red_card=dto_dict.get('red_card'),
            goals=dto_dict.get('goals'),
            possession=dto_dict.get('possession')
        )
        return match_stat
