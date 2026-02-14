import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.asarray(x)

    sigma = 1 / (1 + np.exp(-x))

    swish = x * sigma

    return swish