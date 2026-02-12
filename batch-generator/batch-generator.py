import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here
    X = np.array(X)
    y = np.array(y)
    n = len(X)
    idx = np.arange(n)

    if rng is not None:
        rng.shuffle(idx)
    else:
        np.random.shuffle(idx)

    for i in range(0, n, batch_size):
        batch_idx = idx[i: i+batch_size]

        if drop_last and len(batch_idx) < batch_size:
            break
        
        yield X[batch_idx], y[batch_idx]