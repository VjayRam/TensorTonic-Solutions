import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    res = []

    for i in x:
        if i >= 0:
            res.append(i)
        else:
            res.append(i * alpha)
    
    return np.array(res)
