from .db import db
from sqlalchemy import Column, String, Integer, ForeignKey

class Book(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    pages = Column(Integer, nullable=False)
    author_name = Column(String, nullable=False)

