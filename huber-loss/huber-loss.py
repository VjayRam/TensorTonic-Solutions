import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    e = y_true - y_pred
    abs_e = np.abs(e)

    quad = 0.5 * (e ** 2)
    lin = delta * (abs_e - (0.5 * delta))

    losses = np.where(abs_e <= delta, quad, lin)

    return np.mean(losses)

    