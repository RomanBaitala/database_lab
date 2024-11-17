from __future__ import annotations
from typing import Dict, Any
from app import db
from random import randint, choice
from time import time
from sqlalchemy import text


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


def create_dynamic_tables_from_leagues():
    leagues = League.query.all()
    if not leagues:
        return "No leagues found in the database."

    table_count = randint(1, 9)
    created_tables = []

    for league in leagues[:table_count]:
        league_name = league.name.replace(" ", "_")
        table_name = f"{league_name}_{int(time())}"

        column_defs = []
        for i in range(randint(1, 9)):
            column_name = f"column_{i + 1}"
            column_type = choice(["INT", "VARCHAR(255)", "DATE"])
            column_defs.append(f"{column_name} {column_type}")
        column_defs_str = ", ".join(column_defs)

        create_table_sql = text(f"CREATE TABLE {table_name} (id INT PRIMARY KEY AUTO_INCREMENT, {column_defs_str});")

        db.session.execute(create_table_sql)
        db.session.commit()
        created_tables.append(table_name)

    return created_tables
