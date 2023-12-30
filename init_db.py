from models.base import Base, engine
from models.character import Character  # Import other models as necessary

Base.metadata.create_all(engine)
