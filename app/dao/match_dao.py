from .general_dao import GeneralDAO
from ..domain import FMatch


class MatchDAO(GeneralDAO):
    _domain_type = FMatch
