import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    n = len(y_true)
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    correct_class_probs = y_pred[np.arange(n), y_true]
    losses = -np.log(correct_class_probs)

    return np.mean(losses)