def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    n = len(values)
    output = []
    
    for i in range(n - window_size + 1):
        # 1. Extract the current window
        window = values[i : i + window_size]
        
        # 2. Calculate the mean (mu)
        mean = sum(window) / window_size
        
        output.append(mean)
        
    return output