def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    s1 = set(set_a)
    s2 = set(set_b)

    union = s1 | s2
    intersection = s1 & s2

    if not union:
        return 0.0

    return len(intersection) / len(union)