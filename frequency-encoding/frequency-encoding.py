def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here

    counts = {}
    total = len(values)

    for val in values:
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
    
    return [counts[v] / total for v in values]
        
        