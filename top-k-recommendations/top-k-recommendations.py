def top_k_recommendations(scores, rated_indices, k):
    # 1. Create (score, index) pairs for items NOT in rated_indices
    # We use enumerate to keep track of the original index 'i'
    unrated_items = [
        (scores[i], i) 
        for i in range(len(scores)) 
        if i not in rated_indices
    ]
    
    # 2. Sort by score in descending order
    # x[0] is the score; reverse=True ensures highest scores come first
    unrated_items.sort(key=lambda x: x[0], reverse=True)
    
    # 3. Extract the top k indices
    # If there are fewer than k items, this slicing safely returns all of them
    return [index for score, index in unrated_items[:k]]