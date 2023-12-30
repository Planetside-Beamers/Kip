from models.base import Base, engine
from models.character import Character  # Import other models as necessary

print("Creating database tables...")
Base.metadata.create_all(engine)
print("Database tables created.")

