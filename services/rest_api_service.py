import requests
import json
from controllers.character_controller import process_character_data

API_BASE_URL = "https://census.daybreakgames.com/s:CygnusXAPI/get/ps2:v2"

def fetch_general_character_data(character_id):
    endpoint = f"{API_BASE_URL}/character/"
    params = {"character_id": character_id}

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Raises a HTTPError for bad HTTP status
        return response.json()
    except requests.RequestException as e:
        return {"Error": str(e)}

# Example usage function
def example_usage():
    character_id = "5429091716540847617"  # Example character ID
    character_data = fetch_general_character_data(character_id)
    print(character_data)
    # Assuming process_character_data is adapted for general character data
    process_character_data(character_data)  

if __name__ == "__main__":
    example_usage()
