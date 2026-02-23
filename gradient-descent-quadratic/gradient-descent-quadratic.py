def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x = x0
    # Write code here
    for _ in range(steps):
        gradient = (2 * a * x) + b

        x = x - gradient * lr

    return float(x)