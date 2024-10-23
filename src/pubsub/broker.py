import queue
from matching.matcher import Matcher

class Broker:
    def __init__(self):
        self.event_queue = queue.Queue()
        self.matcher = Matcher()

    def receive_event(self, event):
        self.event_queue.put(event)

    def match_event(self, publisher_event, subscriber_event):
        return self.matcher.match(publisher_event, subscriber_event)

    def forward_event(self, event):
        # Logic to forward the event to matched subscribers
        pass
