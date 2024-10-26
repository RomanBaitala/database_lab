from .general_controller import GeneralController
from ..service import goal_service


class GoalController(GeneralController):
    _service = goal_service
