from .general_controller import GeneralController
from ..service import stadium_service


class StadiumController(GeneralController):
    _service = stadium_service
