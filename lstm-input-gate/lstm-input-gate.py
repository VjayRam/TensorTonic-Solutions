import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def input_gate(h_prev: np.ndarray, x_t: np.ndarray,
               W_i: np.ndarray, b_i: np.ndarray,
               W_c: np.ndarray, b_c: np.ndarray) -> tuple:
    """Compute input gate and candidate memory."""
    # YOUR CODE HERE
    concat = np.concatenate([h_prev, x_t], axis=-1)

    z = concat @ W_i.T + b_i
    
    c = concat @ W_c.T + b_c

    i_t = sigmoid(z)
    c_t = np.tanh(c)

    return i_t, c_t