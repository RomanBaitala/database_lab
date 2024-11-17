from .general_dao import GeneralDAO
from ..domain import Transfer


class TransferDAO(GeneralDAO):
    _domain_type = Transfer
