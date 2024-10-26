from .general_controller import GeneralController
from ..service import match_service


class MatchController(GeneralController):
    _service = match_service
