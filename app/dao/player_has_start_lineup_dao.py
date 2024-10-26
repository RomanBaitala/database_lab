from .general_dao import GeneralDAO
from ..domain import PlayerHasStartLineup


class PlayerHasStartLineupDAO(GeneralDAO):
    _domain_type = PlayerHasStartLineup
