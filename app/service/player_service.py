from .general_service import GeneralService
from ..dao import player_dao


class PlayerService(GeneralService):
    _dao = player_dao
