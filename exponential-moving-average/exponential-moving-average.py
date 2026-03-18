def exponential_moving_average(values, alpha):
    # Initialize with the first value
    ema = [float(values[0])]
    
    # Loop from the second element to the end
    for i in range(1, len(values)):
        # Apply formula: (alpha * current) + ((1 - alpha) * previous_ema)
        current_ema = alpha * values[i] + (1 - alpha) * ema[-1]
        ema.append(current_ema)
        
    return ema