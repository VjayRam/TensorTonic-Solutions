import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    res = np.maximum(0, x)

    if res.ndim == 0:
        return res.reshape(1)

    return res