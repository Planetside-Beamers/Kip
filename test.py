from models.base import engine, Base
from models.character import Character
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

new_character = Character(name="Test Character", total_kills=100, total_deaths=50)
session.add(new_character)
session.commit()

# Query and print out
character = session.query(Character).filter_by(name="Test Character").first()
print(character.name, character.total_kills)