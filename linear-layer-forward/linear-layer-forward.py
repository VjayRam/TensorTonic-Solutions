def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    X = np.array(X)
    W = np.array(W)

    y = X @ W + b

    return y.tolist()