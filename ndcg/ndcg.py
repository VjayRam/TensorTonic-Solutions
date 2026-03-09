import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # If k is larger than the number of items, use all available items
    k = min(k, len(relevance_scores))
    
    def calculate_dcg(scores, cutoff):
        dcg = 0.0
        for i in range(cutoff):
            rel = scores[i]
            # Use the exponential gain formula: 2^rel - 1
            gain = (2 ** rel) - 1
            # Discount using log base 2 of (position + 1), where position is 1-indexed
            # Since i is 0-indexed, we use log2(i + 2)
            discount = math.log2(i + 2)
            dcg += gain / discount
        return dcg

    # 1. Calculate Actual DCG@k
    actual_dcg = calculate_dcg(relevance_scores, k)
    
    # 2. Calculate Ideal DCG@k (IDCG)
    # The ideal ranking is the scores sorted in descending order
    ideal_scores = sorted(relevance_scores, reverse=True)
    ideal_dcg = calculate_dcg(ideal_scores, k)
    
    # 3. Handle edge case: If IDCG is 0 (all relevance scores are zero), return 0.0
    if ideal_dcg == 0:
        return 0.0
        
    return actual_dcg / ideal_dcg