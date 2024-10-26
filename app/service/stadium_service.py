from .general_service import GeneralService
from ..dao import stadium_dao


class StadiumService(GeneralService):
    _dao = stadium_dao
