from .general_controller import GeneralController
from ..service import player_service


class PlayerController(GeneralController):
    _service = player_service
