import numpy as np

def _sigmoid(x):
    """Numerically stable sigmoid function"""
    return np.where(x >= 0, 1.0/(1.0+np.exp(-x)), np.exp(x)/(1.0+np.exp(x)))

def _as2d(a, feat):
    """Convert 1D array to 2D and track if conversion happened"""
    a = np.asarray(a, dtype=float)
    if a.ndim == 1:
        return a.reshape(1, feat), True
    return a, False

def gru_cell_forward(x, h_prev, params):
    """
    Implement the GRU forward pass for one time step.
    Supports shapes (D,) & (H,) or (N,D) & (N,H).
    """
    # Write code here
    # Convert to 2D for consistent matrix math

    x_arr = np.array(x)
    h_arr = np.array(h_prev)
    
    x_2d, x_was_1d = _as2d(x_arr, x_arr.shape[-1])
    h_2d, h_was_1d = _as2d(h_arr, h_arr.shape[-1])

    z_t = _sigmoid(x_2d @ params['Wz'] + h_2d @ params['Uz'] + params['bz'])
    r_t = _sigmoid(x_2d @ params['Wr'] + h_2d @ params['Ur'] + params['br'])

    # Use np.tanh for the candidate state
    h_tilde = np.tanh(x_2d @ params['Wh'] + (r_t * h_2d) @ params['Uh'] + params['bh'])
    h_t = (1 - z_t) * h_2d + z_t * h_tilde
    return h_t.reshape(-1) if x_was_1d else h_t