from .general_service import GeneralService
from ..dao import goal_dao


class GoalService(GeneralService):
    _dao = goal_dao
