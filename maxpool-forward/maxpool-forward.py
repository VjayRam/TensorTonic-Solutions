import numpy as np

def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    X = np.array(X)
    H, W = X.shape
    
    # 1. Compute output dimensions
    out_h = (H - pool_size) // stride + 1
    out_w = (W - pool_size) // stride + 1
    
    # 2. Initialize output
    out = np.zeros((out_h, out_w))
    
    # 3. Slide the window
    for i in range(out_h):
        for j in range(out_w):
            # Define window boundaries
            r_start, r_end = i * stride, i * stride + pool_size
            c_start, c_end = j * stride, j * stride + pool_size
            
            # Extract window and find max
            window = X[r_start:r_end, c_start:c_end]
            out[i, j] = np.max(window)
            
    return out.tolist()