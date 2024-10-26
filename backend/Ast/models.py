from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from typing import List,Dict,Any
class Rule(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    rule_string = fields.TextField()


# Pydantic model for request body validation
class CreateRuleRequest(BaseModel):
    name: str
    rule_string: str


class CombineRulesRequest(BaseModel):
    rules: List[str]


class EvaluateRuleRequest(BaseModel):
    ast: Dict[str, Any]
    data: Dict[str, Any]