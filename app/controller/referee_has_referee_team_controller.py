from .general_controller import GeneralController
from ..service import referee_has_referee_team_service


class RefereeHasRefereeTeamController(GeneralController):
    _service = referee_has_referee_team_service
