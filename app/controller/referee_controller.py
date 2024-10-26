from .general_controller import GeneralController
from ..service import referee_service


class RefereeController(GeneralController):
    _service = referee_service
