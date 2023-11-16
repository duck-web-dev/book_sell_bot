from libs.db.models import *
from libs.db.init import db

db.create_tables([User, Book])

__all__ = ['db']