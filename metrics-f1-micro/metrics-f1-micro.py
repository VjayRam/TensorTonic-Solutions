import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    
    tp = np.sum(y_true == y_pred)

    n = len(y_true)

    fp = n - tp
    fn = n - tp

    denom = (2 * tp) + fp + fn

    if denom == 0:
        return 0

    return float((2 * tp)  / denom)
    