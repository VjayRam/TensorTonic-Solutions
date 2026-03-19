def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here
    rets = []
    w = 1
    for ret in returns:
        w *= (1 + ret)
        c_r = w - 1
        rets.append(c_r)
    return rets