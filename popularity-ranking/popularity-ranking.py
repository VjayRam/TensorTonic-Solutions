def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    res = []
    for R, v in items:
        wr = (v / (v + min_votes)) * R + (min_votes / (v + min_votes)) * global_mean
        res.append(wr)
    return res