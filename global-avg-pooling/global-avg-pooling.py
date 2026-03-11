import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    ndim = x.ndim
    
    if ndim == 3:
        # Average over H (axis 1) and W (axis 2)
        return np.mean(x, axis=(1, 2))
    elif ndim == 4:
        # Average over H (axis 2) and W (axis 3)
        return np.mean(x, axis=(2, 3))
    else:
        raise ValueError(f"Expected 3D or 4D input, got {ndim}D")