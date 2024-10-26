from .general_service import GeneralService
from ..dao import match_stat_dao


class MatchStatService(GeneralService):
    _dao = match_stat_dao
