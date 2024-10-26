from .general_dao import GeneralDAO
from ..domain import MatchStat


class MatchStatDAO(GeneralDAO):
    _domain_type = MatchStat
