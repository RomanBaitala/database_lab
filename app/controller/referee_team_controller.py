from .general_controller import GeneralController
from ..service import referee_team_service


class RefereeTeamController(GeneralController):
    _service = referee_team_service
