import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    y = np.array(y)
    n = y.shape[0]

    if not num_classes:
        num_classes = np.max(y) + 1


    res = np.zeros((n, num_classes))

    res[np.arange(n), y] = 1

    return res
    