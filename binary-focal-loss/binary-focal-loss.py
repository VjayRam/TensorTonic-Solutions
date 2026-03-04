import math

def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    if len(predictions) != len(targets):
        raise ValueError("Length mismatch between predictions and targets")
    fl = 0
    for p, t in zip(predictions, targets):
        if t == 1:
            p_t = p
        else:
            p_t = 1 - p

        fl += - alpha * ((1 - p_t) ** gamma) * math.log(p_t)
    
    return fl / len(predictions)