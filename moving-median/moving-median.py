def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    n = len(values)
    median = []
    for i in range(n - window_size + 1):
        window = sorted(values[i : i + window_size])
        if len(window) % 2 != 0:
            median.append(window[window_size // 2])
        else:
            median.append((window[window_size//2 - 1] + window[window_size//2]) / 2)
    return median
                        