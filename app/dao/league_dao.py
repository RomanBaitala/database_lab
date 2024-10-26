from .general_dao import GeneralDAO
from ..domain import League


class LeagueDAO(GeneralDAO):
    _domain_type = League
