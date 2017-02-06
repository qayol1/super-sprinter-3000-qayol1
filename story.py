from peewee import *

from models import BaseModel


class Story(BaseModel):
    title = CharField()
    description = CharField()
    acceptance_criteria = CharField()
    business_value = IntegerField()
    estimation_hour = FloatField()
    status = CharField()
