from __future__ import annotations
from typing import Dict, Any
from app import db
from sqlalchemy import event, select


class Transfer(db.Model):
    __tablename__ = 'transfers'
    id = db.Column(db.Integer, primary_key=True)
    team_from = db.Column(db.Integer, nullable=False)
    team_to = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return f"Transfer(id='{self.id}', team_from={self.team_from}, team_to={self.team_to}, " \
               f"player_id={self.player_id}, value={self.value}, date={self.date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'team_from': self.team_from,
            'team_to': self.team_to,
            'player_id': self.player_id,
            'value': self.value,
            'date': self.date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Transfer:
        transfer = Transfer(
            team_from=dto_dict.get('team_from'),
            team_to=dto_dict.get('team_to'),
            player_id=dto_dict.get('player_id'),
            value=dto_dict.get('value'),
            date=dto_dict.get('date')
        )
        return transfer


@event.listens_for(Transfer, "before_insert")
def check_team_from_to(mapper, connection, target):
    player_table = db.Table('player', db.metadata, autoload_with=db.engine)
    team_table = db.Table('team', db.metadata, autoload_with=db.engine)

    player_exists = connection.execute(
        select(player_table.c.id).where(player_table.c.id == target.player_id)
    ).first()

    if not player_exists:
        raise ValueError(f"Team with id {target.player_id} does not exist in team table.")

    team_from_exists = connection.execute(
        select(team_table.c.id).where(team_table.c.id == target.team_from)
    ).first()

    if not team_from_exists:
        raise ValueError(f"Team with id {target.team_from} does not exist in team table.")

    team_to_exists = connection.execute(
        select(team_table.c.id).where(team_table.c.id == target.team_to)
    ).first()

    if not team_to_exists:
        raise ValueError(f"Team with id {target.team_to} does not exist in team table.")

