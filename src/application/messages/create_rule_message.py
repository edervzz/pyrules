""" create rule messages """
from typing import List
from domain.entities import Condition, Rule


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(self, name: str, is_zero_condition: bool, kvsid: int, conditions: List[Condition]):
        self.rule = Rule()
        self.rule.name = name
        self.rule.is_zero_condition = is_zero_condition
        self.rule.kvs_id = kvsid

        self.conditions = conditions


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id
