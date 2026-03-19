def double_exponential_smoothing(series, alpha, beta):
    # 1. Initialize
    curr_level = float(series[0])
    curr_trend = float(series[1] - series[0])
    levels = [curr_level]
    
    # 2. Loop through the series starting from t=1
    for t in range(1, len(series)):
        y_t = series[t]
        last_level = curr_level
        
        # Update Level
        curr_level = alpha * y_t + (1 - alpha) * (curr_level + curr_trend)
        
        # Update Trend (uses the NEW level and the OLD level)
        curr_trend = beta * (curr_level - last_level) + (1 - beta) * curr_trend
        
        levels.append(curr_level)
        
    return levels