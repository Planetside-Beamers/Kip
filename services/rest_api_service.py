import requests
import json
from controllers.character_controller import process_character_data

API_BASE_URL = "https://census.daybreakgames.com/s:CygnusXAPI/get/ps2:v2"

def fetch_general_character_data(character_id):
    endpoint = f"{API_BASE_URL}/character/"
    params = {"character_id": character_id}

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"Error": str(e)}
    
def fetch_character_statistics(character_id):
    endpoint = f"{API_BASE_URL}/character/"
    params = {
        "character_id": character_id,
        "c:resolve": "profile"
    }

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"Error": str(e)}

def fetch_world_events(world_id):
    endpoint = f"{API_BASE_URL}/world_event/"
    params = {"world_id": world_id}

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"Error": str(e)}

def fetch_player_online_status(character_id):
    endpoint = f"{API_BASE_URL}/characters_online_status/"
    params = {"character_id": character_id}

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'characters_online_status_list' in data and data['characters_online_status_list']:
            online_status = data['characters_online_status_list'][0].get('online_status', '0')
            return online_status != '0'  # Returns True if online, False otherwise
        return False  # Default to offline if no data found
    except requests.RequestException as e:
        return {"Error": str(e)}


# Example usage function
def example_usage():
    character_id = "5429091716540847617"  # Example character ID
    world_id = "17"

    # character_data = fetch_general_character_data(character_id)
    # print(character_data)
    # process_character_data(character_data) 

    character_statistics_data = fetch_character_statistics(character_id)
    print(character_statistics_data)

    is_online = fetch_player_online_status(character_id)
    print(f"Character {character_id} is {'online' if is_online else 'offline'}.")
     

if __name__ == "__main__":
    example_usage()
