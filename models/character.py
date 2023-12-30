from sqlalchemy import Column, Integer, String
from .base import Base  # Import Base from base.py

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    total_kills = Column(Integer)
    total_deaths = Column(Integer)
