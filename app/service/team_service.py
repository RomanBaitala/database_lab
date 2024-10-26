from .general_service import GeneralService
from ..dao import team_dao


class TeamService(GeneralService):
    _dao = team_dao
