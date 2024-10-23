
class Publisher:
    def __init__(self, broker, user_id):
        self.broker = broker
        self.user_id = user_id

    def publish_event(self, event):
        event_data = {
            'publisher_id': self.user_id,
            'event': event,
        }
        self.broker.receive_event(event_data)
