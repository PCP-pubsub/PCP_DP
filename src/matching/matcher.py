class Matcher:
    def __init__(self):
        pass

    def match(self, publisher_event, subscriber_event):
        """
        Matches the event of the publisher and the interest of the subscriber.
        Publisher and subscriber data contain top-K frequent itemsets.
        """

        publisher_itemsets = publisher_event['top_k_itemsets']
        subscriber_interests = subscriber_event['top_k_itemsets']

        # Matching based on the intersection of top-K itemsets
        matched_itemsets = set(publisher_itemsets).intersection(subscriber_interests)

        if matched_itemsets:
            # If there is any common itemset between the two
            return True
        else:
            return False
