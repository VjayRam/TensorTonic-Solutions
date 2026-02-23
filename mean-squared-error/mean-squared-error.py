import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    if len(y_pred) != len(y_true):
        raise ValidationError
        
    n = len(y_pred)
    sqe = 0

    for i in range(n):
        sqe += (y_pred[i] - y_true[i]) ** 2

    return float(sqe / n)

    
    
