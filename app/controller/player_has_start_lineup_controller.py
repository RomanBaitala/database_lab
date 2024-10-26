from .general_controller import GeneralController
from ..service import player_has_start_lineup_service


class PlayerHasStartLineupController(GeneralController):
    _service = player_has_start_lineup_service
