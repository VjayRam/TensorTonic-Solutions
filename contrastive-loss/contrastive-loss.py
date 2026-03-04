import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here
# Ensure inputs are numpy arrays
    a = np.atleast_2d(a)
    b = np.atleast_2d(b)
    y = np.asarray(y)

    # 1. Compute Euclidean Distance: d = sqrt(sum((a - b)^2))
    # axis=1 computes the norm for each pair in the batch
    distances = np.linalg.norm(a - b, axis=1)

    # 2. Calculate Loss for each pair
    # For y=1 (similar): loss = d^2
    # For y=0 (dissimilar): loss = max(0, margin - d)^2
    pos_loss = y * (distances ** 2)
    neg_loss = (1 - y) * (np.maximum(0, margin - distances) ** 2)
    
    losses = pos_loss + neg_loss

    # 3. Apply reduction
    if reduction == "mean":
        return float(np.mean(losses))
    elif reduction == "sum":
        return float(np.sum(losses))
    else:
        raise ValueError("reduction must be 'mean' or 'sum'")