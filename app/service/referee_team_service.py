from .general_service import GeneralService
from ..dao import referee_team_dao


class RefereeTeamService(GeneralService):
    _dao = referee_team_dao
