import numpy as np

class DifferentialPrivacy:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def exponential_mechanism(self, quality_scores, sensitivity):
        """
        Implements the exponential mechanism for differential privacy.
        
        Args:
            quality_scores (list of tuples): Each tuple is (item, score).
            sensitivity (float): Sensitivity of the quality function.
        
        Returns:
            Selected item with differential privacy.
        """
        # Calculate the probability distribution over the possible outcomes
        probabilities = [np.exp((self.epsilon * score) / (2 * sensitivity)) for _, score in quality_scores]

        # Normalize the probabilities
        total_prob = sum(probabilities)
        normalized_probabilities = [p / total_prob for p in probabilities]

        # Choose an item based on the probability distribution
        items = [item for item, _ in quality_scores]
        selected_item = np.random.choice(items, p=normalized_probabilities)

        return selected_item
