from .general_dao import GeneralDAO
from ..domain import Referee


class RefereeDAO(GeneralDAO):
    _domain_type = Referee
