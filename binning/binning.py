def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    min_val = min(values)
    max_val = max(values)

    if max_val == min_val:
        return [0] * len(values)
    
    bin_width = (max_val - min_val) / num_bins

    res = []

    for v in values:
        bin_idx = int((v - min_val) / bin_width)

        if bin_idx >= num_bins:
            bin_idx = num_bins - 1
        
        res.append(bin_idx)
    
    return res