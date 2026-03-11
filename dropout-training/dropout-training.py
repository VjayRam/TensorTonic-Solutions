import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.array(x)
    if p == 0:
        return x, np.ones_like(x)

    random_val = rng.random(x.shape) if rng else np.random.random(x.shape)

    scale = 1 / (1 - p)

    dropout_pattern = np.where(random_val < (1 - p), scale, 0.0)

    output = x * dropout_pattern

    return output, dropout_pattern