""" Read Workflow """
from typing import List
from domain.entities import Workflow, Rule


class ReadWorkflowRequest:
    """ Read Workflow Request """

    def __init__(self, workflow_id: int, workflow_name: str) -> None:
        self.workflow_id = workflow_id
        self.workflow_name = workflow_name
        self.workflow: Workflow
        self.rules: List[Rule]


class ReadWorkflowResponse:
    """ Read Workflow Response """

    def __init__(self, workflow: Workflow, rules: List[Rule]):
        self.workflow = workflow
        self.rules = rules
