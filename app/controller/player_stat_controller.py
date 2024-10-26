from .general_controller import GeneralController
from ..service import player_stat_service


class PlayerStatController(GeneralController):
    _service = player_stat_service
