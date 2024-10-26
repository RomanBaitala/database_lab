from .general_controller import GeneralController
from ..service import team_service


class TeamController(GeneralController):
    _service = team_service
