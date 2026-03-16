def user_based_cf_prediction(similarities, ratings):
    """
    Predict a rating using user-based collaborative filtering.
    """
    # Write code here
    num = 0
    den = 0 
    for s, r in zip(similarities, ratings):
        if s > 0:
            num += s * r
            den += s

    if den == 0:
        return 0
    else:
        return num / den