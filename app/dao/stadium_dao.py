from .general_dao import GeneralDAO
from ..domain import Stadium


class StadiumDAO(GeneralDAO):
    _domain_type = Stadium
