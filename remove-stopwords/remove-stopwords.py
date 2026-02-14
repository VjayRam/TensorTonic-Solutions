def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    stop_set = set(stopwords)

    res = [token for token in tokens if token not in stop_set]

    return res