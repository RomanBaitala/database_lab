from .general_dao import GeneralDAO
from ..domain import PlayerStat


class PlayerStatDAO(GeneralDAO):
    _domain_type = PlayerStat
