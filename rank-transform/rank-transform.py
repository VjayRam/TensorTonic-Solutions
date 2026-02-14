def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    n = len(values)
    if n == 0:
        return []

    # 1. Create pairs of (value, original_index) and sort them by value
    indexed_values = sorted([(values[i], i) for i in range(n)])
    
    # 2. Initialize the result list
    ranks = [0.0] * n
    
    i = 0
    while i < n:
        j = i
        # 3. Find the range [i, j] of tied values
        while j + 1 < n and indexed_values[j + 1][0] == indexed_values[i][0]:
            j += 1
        
        # 4. Calculate the average rank for this group
        # 1-based positions are (i + 1) and (j + 1)
        avg_rank = (i + 1 + j + 1) / 2.0
        
        # 5. Assign this rank to all indices in the group
        for k in range(i, j + 1):
            original_idx = indexed_values[k][1]
            ranks[original_idx] = avg_rank
            
        # Move to the next group
        i = j + 1
        
    return ranks