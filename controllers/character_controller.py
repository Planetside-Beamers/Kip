from models.character import Character
from models.base import Session
from datetime import datetime

def process_character_data(character_data):
    if 'character_list' not in character_data:
        print("Invalid data format")
        return

    session = Session()
    try:
        for character_info in character_data['character_list']:
            character_id = character_info['character_id']
            name = character_info['name']['first']
            faction_id = character_info['faction_id']
            battle_rank = character_info['battle_rank']['value']
            creation_time = datetime.fromtimestamp(int(character_info['times']['creation']))
            last_login_time = datetime.fromtimestamp(int(character_info['times']['last_login']))
            login_count = int(character_info['times']['login_count'])
            minutes_played = int(character_info['times']['minutes_played'])

            character = session.query(Character).filter_by(character_id=character_id).first()
            if character:
                # Update existing character
                character.name = name
                character.faction_id = faction_id
                character.battle_rank = battle_rank
                character.creation_time = creation_time
                character.last_login_time = last_login_time
                character.login_count = login_count
                character.minutes_played = minutes_played
            else:
                # Create new character
                character = Character(character_id, name, faction_id, battle_rank, creation_time, last_login_time, login_count, minutes_played)
                session.add(character)

        session.commit()
    except Exception as e:
        print(f"Error processing character data: {e}")
        session.rollback()
    finally:
        session.close()
