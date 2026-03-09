import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    losses = []
    
    for y, p in zip(y_true, y_pred):
        # 1. Clip the prediction to prevent log(0) or log(1)
        # p_clipped = max(eps, min(1 - eps, p))
        p_hat = min(max(p, eps), 1 - eps)
        
        # 2. Apply the binary cross-entropy formula:
        # L = -(y * ln(p_hat) + (1 - y) * ln(1 - p_hat))
        sample_loss = -(y * math.log(p_hat) + (1 - y) * math.log(1 - p_hat))
        
        losses.append(sample_loss)
        
    return losses