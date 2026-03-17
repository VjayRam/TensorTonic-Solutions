def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    n = len(series)
    mean = sum(series) / n

    gamma_0 = sum((x - mean) ** 2 for x in series)

    if gamma_0 == 0:
        return [1.0] + [0.0] * max_lag

    res = []

    for k in range(max_lag + 1):

        autocovariance_k = sum((series[t] - mean) * (series[t + k] - mean) for t in range(n - k))

        rk = autocovariance_k / gamma_0
        res.append(rk)

    return res

    