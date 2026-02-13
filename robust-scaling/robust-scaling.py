import numpy as np

def robust_scaling(values):
    # 1. Sort the values (Crucial for manual median/quartile calculation)
    v_sorted = sorted(values)
    n = len(v_sorted)
    
    # Helper to find median of a list
    def get_median(arr):
        size = len(arr)
        if size == 0: return 0
        mid = size // 2
        if size % 2 == 0:
            return (arr[mid - 1] + arr[mid]) / 2
        return arr[mid]

    # 2. Calculate the global Median
    median = get_median(v_sorted)
    
    # 3. Determine halves to find Q1 and Q3
    mid_idx = n // 2
    if n % 2 == 0:
        lower_half = v_sorted[:mid_idx]
        upper_half = v_sorted[mid_idx:]
    else:
        # For odd length, exclude the middle element from both halves
        lower_half = v_sorted[:mid_idx]
        upper_half = v_sorted[mid_idx + 1:]
        
    q1 = get_median(lower_half)
    q3 = get_median(upper_half)
    
    # 4. Calculate IQR and Scale
    iqr = q3 - q1
    
    res = []
    for v in values:
        if iqr == 0:
            res.append(float(v - median))
        else:
            res.append(float((v - median) / iqr))
            
    return res