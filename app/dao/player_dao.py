from .general_dao import GeneralDAO
from ..domain import Player


class PlayerDAO(GeneralDAO):
    _domain_type = Player
