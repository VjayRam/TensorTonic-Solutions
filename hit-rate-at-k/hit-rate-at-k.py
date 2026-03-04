def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    if not recommendations:
        return 0.0
        
    hits = 0
    num_users = len(recommendations)

    for i in range(num_users):
        top_k = set(recommendations[i][:k])

        relevant = set(ground_truth[i])

        if top_k & relevant:
            hits += 1

    return hits / num_users
    
        