import numpy as np

def rnn_step_backward(dh, cache):
    # 1. Unpack cache and convert everything to numpy arrays
    # This prevents 'list' object errors with math operators
    x_t = np.array(cache[0])
    h_prev = np.array(cache[1])
    h_t = np.array(cache[2])
    W = np.array(cache[3])
    U = np.array(cache[4])
    b = np.array(cache[5])
    dh = np.array(dh)

    # 2. Tanh gradient (dz)
    # Using the formula: dz = dh * (1 - h_t^2)
    dz = dh * (1 - h_t**2)
    
    # 3. Gradients for weights and bias
    # dW = dz (H,1) outer product with x_t (D,1) -> (H, D)
    # dU = dz (H,1) outer product with h_prev (H,1) -> (H, H)
    dW = np.outer(dz, x_t)
    dU = np.outer(dz, h_prev)
    db = dz  # Bias gradient is just dz for a single step
    
    # 4. Gradients for inputs and previous hidden state
    # dx_t = dz (H) dot W (H, D) -> (D,)
    # dh_prev = dz (H) dot U (H, H) -> (H,)
    dx_t = dz @ W
    dh_prev = dz @ U
    
    return dx_t, dh_prev, dW, dU, db