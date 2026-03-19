import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X = np.array(X)
    y = np.array(y)

    X_tX = np.linalg.inv(X.T @ X)

    w = X_tX @ X.T @ y

    return w