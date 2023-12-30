# character_controller.py

from models.character import Character  # Assuming Character is a model in your database
from models.base import Session

def process_character_data(character_data):
    if 'characters_event_list' not in character_data:
        print("Invalid data format")
        return

    session = Session()
    try:
        for event in character_data['characters_event_list']:
            # Extract character name and other relevant information
            character_name = event['character']['name']['first']
            # Extract more fields as needed, e.g., kills, deaths, etc.
            # Assuming these fields exist in your Character model
            character = Character(name=character_name)
            # Add more fields as per your model
            session.add(character)

        session.commit()
    except Exception as e:
        print(f"Error processing character data: {e}")
        session.rollback()
    finally:
        session.close()

