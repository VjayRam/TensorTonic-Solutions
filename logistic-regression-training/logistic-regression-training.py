import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    n_samples, n_feat = X.shape

    w = np.zeros(n_feat)
    b = 0.0

    for _ in range(steps):
        z = np.dot(X, w) + b
        p = _sigmoid(z)

        error = p - y

        dw = np.dot(X.T, error) / n_samples
        db = np.mean(error)

        w -= lr * dw
        b -= lr * db

    return w, b