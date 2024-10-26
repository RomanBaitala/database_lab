from .general_service import GeneralService
from ..dao import referee_has_referee_team_dao


class RefereeHasRefereeTeamService(GeneralService):
    _dao = referee_has_referee_team_dao
