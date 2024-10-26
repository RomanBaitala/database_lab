from .general_service import GeneralService
from ..dao import match_dao


class MatchService(GeneralService):
    _dao = match_dao
