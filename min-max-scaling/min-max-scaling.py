import numpy as np

def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    data = np.array(data, dtype=float)
    
    # 1. Compute min and max with keepdims=True for broadcasting
    x_min = np.min(data, axis=0, keepdims=True)
    x_max = np.max(data, axis=0, keepdims=True)
    
    # 2. Calculate the range
    diff = x_max - x_min
    
    # 3. FIX: Use np.maximum (element-wise) instead of np.max
    denom = np.maximum(diff, 1)
    
    # 4. Normalize
    X_scaled = (data - x_min) / denom
    
    return X_scaled.tolist()