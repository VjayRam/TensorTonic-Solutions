def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    W = np.array(W)
    limit = np.sqrt(6 / fan_in)

    W_new = (W * (2 * limit)) - limit 

    return W_new

    