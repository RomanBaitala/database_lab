from .general_dao import GeneralDAO
from ..domain import RefereeTeam


class RefereeTeamDAO(GeneralDAO):
    _domain_type = RefereeTeam
