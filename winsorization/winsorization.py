import math

def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds using linear interpolation.
    """
    if not values:
        return []

    # 1. Create a sorted version to find percentile values
    sorted_values = sorted(values)
    n = len(sorted_values)

    def get_percentile(p):
        # Formula: k = (n - 1) * p / 100
        k = (n - 1) * p / 100
        floor_idx = math.floor(k)
        ceil_idx = math.ceil(k)
        
        # Linear Interpolation: 
        # value = arr[floor] + (k - floor) * (arr[ceil] - arr[floor])
        fraction = k - floor_idx
        return sorted_values[floor_idx] + fraction * (sorted_values[ceil_idx] - sorted_values[floor_idx])

    # 2. Calculate the exact float boundaries
    lower_bound = get_percentile(lower_pct)
    upper_bound = get_percentile(upper_pct)

    # 3. Clip the original values (preserving original order)
    res = []
    for x in values:
        if x < lower_bound:
            res.append(float(lower_bound))
        elif x > upper_bound:
            res.append(float(upper_bound))
        else:
            res.append(float(x))
            
    return res