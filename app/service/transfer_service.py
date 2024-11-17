from .general_service import GeneralService
from ..dao import transfer_dao


class TransferService(GeneralService):
    _dao = transfer_dao
