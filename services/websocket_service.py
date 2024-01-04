import json
import websocket
from controllers.event_controller import process_event_data  # Import your event processing function

def combine_zone_instance_ids(definition_id, instance_id):
    # Shift instance ID 16 bits to the left and combine with definition ID
    combined_id = (instance_id << 16) | definition_id
    return combined_id

def on_message(ws, message):
    try:
        event_data = json.loads(message)
        process_event_data(event_data)  # Use the controller function to process data
    except Exception as e:
        print(f"Error processing message: {e}")

def on_error(ws, error):
    print("WebSocket Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("### WebSocket Closed ###")

def on_open(ws):
    print("Opening Connection")

    worlds = ["17"]  # Server
    definition_id = 10  # Continent
    instance_id = 16  # Instance - can be set to blank
    eventNames = ["all"]  # Events to subscribe to
    characters = ["all"]  # Characters to listen to events for
    charactersAndWorld = False
    combined_zone_id = combine_zone_instance_ids(definition_id, instance_id) if instance_id else definition_id

    clear_message = {
        "service": "event",
        "action": "clearSubscribe",
        "all": "true"
    }

    subscribe_message = {
        "service": "event",
        "action": "subscribe",
        "worlds": ["17"],
        "eventNames": ["all"],
        "characters": ["all"],
        "logicalAndCharactersWithWorlds": "true"
    }

    if definition_id:
        subscribe_message["zones"] = [str(combined_zone_id)]

    # if characters:
    #     subscribe_message["characters"] = characters

    # if charactersAndWorld:
    #     subscribe_message["logicalAndCharactersWithWorlds"] = "true"

    ws.send(json.dumps(clear_message))
    ws.send(json.dumps(subscribe_message))

def setup_websocket_connection():
    ws = websocket.WebSocketApp(f"wss://push.planetside2.com/streaming?environment=ps2&service-id=s:CygnusXAPI",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

if __name__ == "__main__":
    websocket.enableTrace(True)
    setup_websocket_connection()
