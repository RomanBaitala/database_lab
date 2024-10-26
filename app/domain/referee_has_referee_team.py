from __future__ import annotations
from typing import Dict, Any
from app import db


class RefereeHasRefereeTeam(db.Model):
    __tablename__ = 'referee_has_referee_team'
    id = db.Column(db.Integer, primary_key=True)
    referee_id = db.Column(db.Integer, db.ForeignKey('referee.id'), nullable=False)
    referee_team_id = db.Column(db.Integer, db.ForeignKey('referee_team.id'), nullable=False)

    def __repr__(self) -> str:
        return (f"RefereeHasRefereeTeam(id='{self.id}', referee_id='{self.referee_id}', "
                f"referee_team_id='{self.referee_team_id}')")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'referee_id': self.referee_id,
            'referee_team_id': self.referee_team_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RefereeHasRefereeTeam:
        referee_has_referee_team = RefereeHasRefereeTeam(
            referee_id=dto_dict.get('referee_id'),
            referee_team_id=dto_dict.get('referee_team_id'),
        )
        return referee_has_referee_team
