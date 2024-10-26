from .general_service import GeneralService
from ..dao import referee_dao


class RefereeService(GeneralService):
    _dao = referee_dao
