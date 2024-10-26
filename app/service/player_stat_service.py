from .general_service import GeneralService
from ..dao import player_stat_dao


class PlayerStatService(GeneralService):
    _dao = player_stat_dao
