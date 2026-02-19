import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Convert to numpy arrays and ensure 2D (N, D)
    a = np.atleast_2d(anchor)
    p = np.atleast_2d(positive)
    n = np.atleast_2d(negative)
    
    # Compute squared Euclidean distances: ||x - y||^2
    # axis=1 computes the sum across the embedding dimensions
    dist_pos = np.sum(np.square(a - p), axis=1)
    dist_neg = np.sum(np.square(a - n), axis=1)
    
    # Triplet loss formula: max(0, d(a,p) - d(a,n) + margin)
    losses = np.maximum(0, dist_pos - dist_neg + margin)
    
    # Return the scalar mean loss across the batch
    return np.mean(losses)