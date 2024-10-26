from .general_dao import GeneralDAO
from ..domain import StartLineup


class StartLineupDAO(GeneralDAO):
    _domain_type = StartLineup
