import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    order = {v: i for i, v in enumerate(vocab)}

    counts = np.zeros(len(vocab), dtype=int)

    for t in tokens:
        if t in order:
            idx = order[t]
            counts[idx] += 1

    return counts