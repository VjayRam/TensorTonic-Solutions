import math

def rolling_std(values, window_size):
    n = len(values)
    output = []
    
    for i in range(n - window_size + 1):
        # 1. Extract the current window
        window = values[i : i + window_size]
        
        # 2. Calculate the mean (mu)
        mean = sum(window) / window_size
        
        # 3. Calculate population variance
        # Sum of squared differences from the mean, divided by k
        variance = sum((x - mean) ** 2 for x in window) / window_size
        
        # 4. Calculate standard deviation (sqrt of variance)
        std_dev = math.sqrt(variance)
        output.append(std_dev)
        
    return output