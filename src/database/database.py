from peewee import *

db = SqliteDatabase("../../todos.db")


class Base(Model):
	class Meta:
		database = db


class Todos(Base):
	id = AutoField(primary_key=True)
	title = CharField(max_length=36)
	desc = CharField(max_length=128)
	important = BooleanField(default=False)
	complete = BooleanField(default=False)

