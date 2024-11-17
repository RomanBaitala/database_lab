from .general_controller import GeneralController
from ..service import transfer_service


class TransferController(GeneralController):
    _service = transfer_service
