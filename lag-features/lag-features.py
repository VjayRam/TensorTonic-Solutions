def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here
    res = []

    max_lag = max(lags)

    for t in range(max_lag, len(series)):
        row = [series[t - lag] for lag in lags]
        res.append(row)
    
    return res
