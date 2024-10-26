from __future__ import annotations
from typing import Dict, Any
from app import db


class RefereeTeam(db.Model):
    __tablename__ = 'referee_team'

    id = db.Column(db.Integer, primary_key=True)
    referee_qty = db.Column(db.Integer, nullable=False)
    referees = db.relationship('Referee', secondary='referee_has_referee_team', back_populates='referee_team')

    def __repr__(self) -> str:
        return f"RefereeTeam(id='{self.id}', referee_qty='{self.referee_qty}')"

    def put_into_dto(self) -> Dict[str, Any]:
        referees = [referee.put_into_dto() for referee in self.referees]
        return {
            'id': self.id,
            'referee_qty': self.referee_qty,
            'referees': referees if referees else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RefereeTeam:
        referee_team = RefereeTeam(
            referee_qty=dto_dict.get('referee_qty'),
        )
        return referee_team
