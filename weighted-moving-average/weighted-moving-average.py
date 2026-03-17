def weighted_moving_average(values, weights):
    n = len(values)
    k = len(weights)
    w_sum = sum(weights)
    
    results = []
    
    # Iterate through each valid window start position
    for i in range(n - k + 1):
        # Calculate the weighted sum for the current window
        current_window_sum = 0
        for j in range(k):
            current_window_sum += values[i + j] * weights[j]
            
        # Normalize and add to results
        results.append(current_window_sum / w_sum)
        
    return results