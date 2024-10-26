from .general_dao import GeneralDAO
from ..domain import RefereeHasRefereeTeam


class RefereeHasRefereeTeamDAO(GeneralDAO):
    _domain_type = RefereeHasRefereeTeam
