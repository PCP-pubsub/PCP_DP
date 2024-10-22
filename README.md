# PCP Project: Privacy-Preserving Content-Based Publish/Subscribe Scheme

## Overview

This project implements a **Privacy-Preserving Content-Based Publish/Subscribe (PCP) Scheme** with differential privacy in the context of fog computing. The system uses a combination of **differential privacy** mechanisms and the **U-Apriori algorithm** to ensure that sensitive information in publish/subscribe systems remains secure while allowing efficient event matching.

### Features:

- **Differential Privacy**: Adds privacy-preserving noise to sensitive data using the Laplace and exponential mechanisms.
- **U-Apriori Algorithm**: Mines the top-K frequent itemsets from uncertain datasets.
- **Event Matching**: Matches subscribers and publishers based on their attributes while ensuring privacy.
- **Fog-Based Architecture**: Utilizes fog nodes as brokers for scalable publish/subscribe communication.

### Requirements

- `python 3.x`
- `numpy` python library

### Getting Started

#### 1. Clone the Repository

```bash
git clone https://github.com/PCP-pubsub/PCP_DP.git
cd PCP_DP
```

#### 2. Add sample dataset (optional)

You can add a sample dataset for testing the U-Apriori algorithm in the data/datasets folder. Ensure that it's in the form of a list of transactions with probabilities (for uncertain datasets).

#### 3. Running the project

**Example usage** 

The following is an example of how to use the broker to register subscribers, publish events, and match them based on their interests.

```python
from pubsub.broker import Broker
from pubsub.publisher import Publisher
from pubsub.subscriber import Subscriber

# Initialize broker
broker = Broker()

# Register subscribers
subscriber1 = {'id': 1, 'interest': {'top_k_itemsets': ['item2', 'item3']}}
subscriber2 = {'id': 2, 'interest': {'top_k_itemsets': ['item4', 'item5']}}

broker.add_subscriber(subscriber1)
broker.add_subscriber(subscriber2)

# Publisher publishes an event
publisher_event = {'event': 'New Event', 'top_k_itemsets': ['item2', 'item6']}
broker.receive_event(publisher_event)

# Forward event to matching subscribers
broker.forward_event(publisher_event)
```

#### 4. Running Tests

The project includes unti tests to ensure that the publish/subscribe system, differential privacy and U-Apriori algorithm work correctly.

To run the tests, use:

```bash
python -m unittest src/tests/test_pubsub.py
```

### How the System Works

1. **Event Production**:

    - Publishers generate events with attributes (represented as top-K itemsets) and send them to the broker.

2. **Event Matching**:

    - The broker matches the event's attributes (itemsets) against subscribers' interests using the Matcher.

3. **Differential Privacy**:

    - Differential privacy ensures that sensitive data from publishers and subscribers cannot be leaked during event matching.

4. **Event Forwarding**:

    - The broker forwards events only to the subscribers whose interests match the event attributes.

### Future Improvements
- Support for more complex data types in event matching.
- Integration with a real message queue for scalable event forwarding.
- Optimization of the U-Apriori algorithm for larger datasets.
- Advanced logging and monitoring for better error tracking and fault tolerance.

### License

This project is licensed under the MIT License. Feel free to modify and distribute as needed.

