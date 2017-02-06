from peewee import *

with open('/home/peter/python/first_flask_homework/dbopen.txt', 'r') as f:
    db = PostgresqlDatabase(f.readline()[:-1])

class BaseModel(Model):
    class Meta:
        database = db
