from models.base import Base, engine
from models.character import Character  # Import other models

Base.metadata.create_all(engine)
