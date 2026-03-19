def seasonal_average(series, period):
    seasonal_means = []
    
    for p in range(period):
        # 1. Collect all values that fall into this seasonal position
        # Start at p, go to the end, skip by 'period'
        position_values = [series[i] for i in range(p, len(series), period)]
        
        # 2. Calculate the average for this position
        avg = sum(position_values) / len(position_values)
        
        # 3. Add to our final list
        seasonal_means.append(float(avg))
        
    return seasonal_means