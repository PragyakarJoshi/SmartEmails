from peewee import *

db = SqliteDatabase('Emails.db')

class Emails(Model):
    id = IntegerField(primary_key=True)
    sender = TextField()
    subject = TextField()
    content = TextField()
    category = TextField()

    class Meta:
        database = db

def initialize_db():
    db.connect()
    db.create_tables([Emails], safe=True)
