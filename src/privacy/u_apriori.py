from collections import defaultdict
from itertools import combinations
import numpy as np

class UApriori:
    def __init__(self, dataset):
        self.dataset = dataset

    def mine_top_k(self, k, min_support):
        """
        Mines the top-K frequent itemsets from the uncertain dataset using U-Apriori.

        Args:
            k (int): The number of top frequent itemsets to find.
            min_support (float): The minimum support threshold.
        
        Returns:
            List of top-K frequent itemsets.
        """
        # Step 1: Calculate expected support for all itemsets
        itemsets_support = self.calculate_expected_support()

        # Step 2: Filter itemsets by minimum support
        frequent_itemsets = {itemset: support for itemset, support in itemsets_support.items() if support >= min_support}

        # Step 3: Sort the itemsets by their support
        sorted_itemsets = sorted(frequent_itemsets.items(), key=lambda x: x[1], reverse=True)

        # Step 4: Return the top-K itemsets
        top_k_itemsets = [itemset for itemset, _ in sorted_itemsets[:k]]

        return top_k_itemsets

    def calculate_expected_support(self):
        """
        Calculate the expected support for each itemset in the dataset.
        
        Returns:
            A dictionary where keys are itemsets and values are their expected support.
        """
        itemsets_support = defaultdict(float)

        for transaction in self.dataset:
            for itemset in self.generate_itemsets(transaction):
                probability = self.calculate_probability(itemset, transaction)
                itemsets_support[itemset] += probability

        return itemsets_support

    def generate_itemsets(self, transaction):
        """
        Generates all possible itemsets from a transaction.
        This is a placeholder; it can be optimized for specific use cases.
        """
        items = list(transaction.keys())
        itemsets = []
        # Generate all subsets of items (excluding the empty set)
        for i in range(1, len(items) + 1):
            itemsets.extend([frozenset(comb) for comb in combinations(items, i)])
        return itemsets

    def calculate_probability(self, itemset, transaction):
        """
        Calculate the probability of an itemset occurring in a transaction.
        """
        probability = 1.0
        for item in itemset:
            probability *= transaction[item]  # Probability of the item being in the transaction
        return probability
