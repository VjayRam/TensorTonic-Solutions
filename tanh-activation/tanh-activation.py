import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)
    num = np.exp(x) - np.exp(-x)
    denom = np.exp(x) + np.exp(-x)
    return num / denom