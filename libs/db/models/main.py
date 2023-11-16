from peewee import Model
from peewee import IntegerField, FloatField, BooleanField, TextField, ForeignKeyField
from libs.db.init import db


class Book(Model):
    id		= IntegerField(unique=True, primary_key=True)
    name	= TextField(null=False)
    img_url	= TextField(null=False)
    price	= FloatField(null=False)

    class Meta:
        database = db


class User(Model):
    id			= IntegerField(unique=True, primary_key=True)
    balance		= FloatField(default=0)
    purchases	= ForeignKeyField(Book, backref='purchases', null=True)
    is_admin	= BooleanField(default=False)

    class Meta:
        database = db