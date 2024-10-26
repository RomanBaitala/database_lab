from .general_controller import GeneralController
from ..service import match_stat_service


class MatchStatController(GeneralController):
    _service = match_stat_service
