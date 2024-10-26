from .general_dao import GeneralDAO
from ..domain import Team


class TeamDAO(GeneralDAO):
    _domain_type = Team
