from .general_dao import GeneralDAO
from ..domain import Goal


class GoalDAO(GeneralDAO):
    _domain_type = Goal
