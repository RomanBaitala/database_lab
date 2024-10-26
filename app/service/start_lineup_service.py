from .general_service import GeneralService
from ..dao import start_lineup_dao


class StartLineupService(GeneralService):
    _dao = start_lineup_dao
