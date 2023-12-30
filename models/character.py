from sqlalchemy import Column, Integer, String, DateTime
from .base import Base  # Import Base from base.py

class Character(Base):
    __tablename__ = 'characters'

    character_id = Column(String, primary_key=True)
    name = Column(String)
    faction_id = Column(Integer)
    battle_rank = Column(Integer)
    creation_time = Column(DateTime)
    last_login_time = Column(DateTime)
    login_count = Column(Integer)
    minutes_played = Column(Integer)
    # Additional fields can be added based on your requirements

    def __init__(self, character_id, name, faction_id, battle_rank, creation_time, last_login_time, login_count, minutes_played):
        self.character_id = character_id
        self.name = name
        self.faction_id = faction_id
        self.battle_rank = battle_rank
        self.creation_time = creation_time
        self.last_login_time = last_login_time
        self.login_count = login_count
        self.minutes_played = minutes_played

    def __repr__(self):
        return f"<Character(name={self.name}, faction_id={self.faction_id}, battle_rank={self.battle_rank})>"
