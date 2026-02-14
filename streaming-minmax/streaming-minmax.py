import numpy as np

def streaming_minmax_init(D):
    """
    Initialize state dict with min, max arrays of shape (D,).
    Starts with +inf and -inf so any real data will overwrite them.
    """
    min_arr = np.full(D, np.inf)
    max_arr = np.full(D, -np.inf)
    return {"min": min_arr, "max": max_arr}

def streaming_minmax_update(state, X_batch, eps=1e-8):
    """
    Update state's min/max with X_batch, return normalized batch.
    """
    X_batch = np.array(X_batch)
    
    # 1. Calculate min and max for the current batch
    batch_min = np.min(X_batch, axis=0)
    batch_max = np.max(X_batch, axis=0)
    
    # 2. Update the global state with the new batch statistics
    state['min'] = np.minimum(state['min'], batch_min)
    state['max'] = np.maximum(state['max'], batch_max)
    
    # 3. Calculate the range (denominator) including epsilon to avoid div by zero
    # Formula: x' = (x - min) / (max - min + eps)
    diff = (state['max'] - state['min']) + eps
    
    # 4. Normalize the batch using the updated global statistics
    X_normalized = (X_batch - state['min']) / diff
    
    return X_normalized