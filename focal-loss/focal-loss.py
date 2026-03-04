import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p = np.array(p)
    p = np.clip(p, 1e-15, 1 - 1e-15)
    y = np.array(y)

    p1 = -((1 - p) ** gamma) * y * np.log(p) 
    p2 = -(p ** gamma) * (1 - y) * np.log(1 - p)

    fl = p1 + p2

    return np.mean(fl)