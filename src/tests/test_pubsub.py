
import unittest
from pubsub.broker import Broker
from pubsub.publisher import Publisher
from pubsub.subscriber import Subscriber
from matching.matcher import Matcher
from privacy.differential_privacy import DifferentialPrivacy
from privacy.u_apriori import UApriori

class TestPubSub(unittest.TestCase):
    def test_event_flow(self):
        broker = Broker()
        publisher = Publisher(broker, user_id=1)
        subscriber = Subscriber(broker, user_id=2, interest="topic1")

        publisher.publish_event("topic1")
        matched = broker.match_event({'event': 'topic1'}, {'interest': 'topic1'})
        self.assertTrue(matched)

    def test_match(self):
        matcher = Matcher()
        publisher_event = {'top_k_itemsets': ['item1', 'item2', 'item3']}
        subscriber_event = {'top_k_itemsets': ['item2', 'item4', 'item5']}

        self.assertTrue(matcher.match(publisher_event, subscriber_event))
        self.assertFalse(matcher.match(publisher_event, {'top_k_itemsets': ['item6', 'item7']}))

    def test_exponential_mechanism(self):
        dp = DifferentialPrivacy(epsilon=1.0)
        quality_scores = [('option1', 0.8), ('option2', 0.4), ('option3', 0.9)]
        sensitivity = 1.0

        selected_item = dp.exponential_mechanism(quality_scores, sensitivity)
        self.assertIn(selected_item, [option for option, score in quality_scores])

    def test_mine_top_k(self):
        dataset = [
                {'item1': 0.9, 'item2': 0.8},
                {'item1': 0.5, 'item2': 0.3, 'item3': 0.6},
                {'item2': 0.7, 'item3': 0.8},
                ]
        uapriori = UApriori(dataset)
        top_k = uapriori.mine_top_k(k=2, min_support=0.5)

        # Test if top-k frequent itemsets are correctly identified
        self.assertIn(frozenset(['item1']), top_k)
        self.assertIn(frozenset(['item2']), top_k)

if __name__ == '__main__':
    unittest.main()
