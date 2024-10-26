from .general_service import GeneralService
from ..dao import league_dao


class LeagueService(GeneralService):
    _dao = league_dao
