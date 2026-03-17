import math

def novelty_score(recommendations, item_counts, n_users):
    """
    Compute the average novelty of a recommendation list.
    """
    if not recommendations:
        return 0.0
    
    total_novelty = 0.0
    
    for item_id in recommendations:
        # 1. Get the number of users who interacted with this specific item
        count_i = item_counts[item_id]
        
        # 2. Calculate popularity (probability of interaction)
        popularity = count_i / n_users
        
        # 3. Calculate self-information using log base 2
        # novelty = -log2(count_i / N)
        total_novelty += -math.log2(popularity)
        
    # 4. Return the average novelty across all recommended items
    return total_novelty / len(recommendations)