# controllers/event_controller.py

from models.base import Session

def process_event_data(event_data):
    session = Session()
    try:
        # Assuming event_data is a dictionary containing event attributes
        new_event = Event(event_data)
        session.add(new_event)
        session.commit()
    except Exception as e:
        print(f"Error processing event data: {e}")
        session.rollback()
    finally:
        session.close()