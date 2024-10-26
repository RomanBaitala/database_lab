from .general_service import GeneralService
from ..dao import player_has_start_lineup_dao


class PlayerHasStartLineupService(GeneralService):
    _dao = player_has_start_lineup_dao
