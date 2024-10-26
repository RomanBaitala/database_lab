from .general_controller import GeneralController
from ..service import start_lineup_service


class StartLineupController(GeneralController):
    _service = start_lineup_service
