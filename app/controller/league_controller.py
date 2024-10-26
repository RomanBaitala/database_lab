from .general_controller import GeneralController
from ..service import league_service


class LeagueController(GeneralController):
    _service = league_service
