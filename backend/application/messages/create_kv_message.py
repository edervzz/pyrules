""" Create Container messages
    """
from domain.entities import KV


class CreateKVRequest:
    """_summary_"""

    def __init__(self, name: str):
        self.kv = KV()
        self.kv.name = name
        self.kv.version = 1


class CreateKVResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id
