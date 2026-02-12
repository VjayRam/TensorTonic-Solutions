import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    # Write code here
    idx = np.arange(N)

    if shuffle:
        if rng is not None:
            idx = rng.permutation(idx)
        else:
            np.random.shuffle(idx)

    folds = np.array_split(idx, k)

    results = []

    for i in range(k):
        val_idx = folds[i]

        train_folds = [folds[j] for j in range(k) if j != i]
        train_idx = np.concatenate(train_folds)

        results.append((train_idx, val_idx))

    return results
