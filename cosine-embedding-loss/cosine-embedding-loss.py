def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    dot = sum(a * b for a, b in zip(x1, x2))

    norm_1 = math.sqrt(sum(a * a for a in x1))
    norm_2 = math.sqrt(sum(a * a for a in x2))

    cosine = float(dot / (norm_1 * norm_2))

    if label == 1:
        loss = 1 - cosine
    elif label == -1:
        loss = max(0, cosine - margin)
    else:
        raise ValueError("invalid label")

    return loss