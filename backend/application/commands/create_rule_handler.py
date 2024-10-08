r"""_summary_"""
import logging
from application.messages import CreateRuleRequest, CreateRuleResponse
from application.validators import CreateRuleValidator, CreateRuleBizValidator
from domain.ports import CoreRepository
from domain.entities import Rule
from toolkit import Localizer


class CreateRuleHandler:
    r""" _summary_ """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer
        self.rule: Rule = None

    def handler(self, request: CreateRuleRequest) -> CreateRuleResponse:
        r""" Handler """
        # 1. request validation
        validator = CreateRuleValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business rule validation
        biz_validator = CreateRuleBizValidator(self.repository, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        self.repository.begin()
        self.repository.rule.create(request.rule)
        for e in request.kvs:
            self.repository.kvs.create(e)
        for e in request.kvitems:
            self.repository.kvitem.create(e)
        for e in request.conditions:
            self.repository.condition.create(e)
        for e in request.expressions:
            self.repository.expression.create(e)

        self.repository.commit_work()

        return CreateRuleResponse(request.rule.id)
