import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.array(x)
    gamma = np.array(gamma)
    beta = np.array(beta)
    
    ndim = x.ndim
    if ndim == 2:
        axes = (0,)
        gamma_cfg = gamma
        beta_cfg = beta
    elif ndim == 4:
        axes = (0, 2, 3)
        gamma_cfg = gamma.reshape(1, -1, 1, 1)
        beta_cfg = beta.reshape(1, -1, 1, 1)
    else:
        raise ValueError("Unsupported input shape")

    mean = np.mean(x, axis=axes, keepdims=True)
    var = np.var(x, axis=axes, keepdims=True)

    x_hat = (x - mean) / np.sqrt(var + eps)

    out = gamma_cfg * x_hat + beta_cfg

    return out
    