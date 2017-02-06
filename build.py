from models import *
from story import Story


class Build:
    @staticmethod
    def create_table():
        db.connect()
        db.create_tables([Story], safe=True)
