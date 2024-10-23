
class Subscriber:
    def __init__(self, broker, user_id, interest):
        self.broker = broker
        self.user_id = user_id
        self.interest = interest

    def subscribe(self):
        subscriber_data = {
            'subscriber_id': self.user_id,
            'interest': self.interest,
        }
        self.broker.receive_event(subscriber_data)
