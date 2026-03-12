import numpy as np

def _dot(a, b):
    """Dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))

def lbfgs_direction(grad, s_list, y_list):
    """
    Compute the L-BFGS search direction using the two-loop recursion.
    """
    # 1. Convert inputs to numpy arrays for vector arithmetic
    q = np.array(grad, dtype=float)
    S = [np.array(s, dtype=float) for s in s_list]
    Y = [np.array(y, dtype=float) for y in y_list]
    m = len(S)
    
    alphas = [0.0] * m
    rhos = [0.0] * m
    
    # 2. Backward loop: newest history (m-1) down to oldest (0)
    for i in reversed(range(m)):
        rhos[i] = 1.0 / np.dot(Y[i], S[i])
        alphas[i] = rhos[i] * np.dot(S[i], q)
        q = q - alphas[i] * Y[i]
        
    # 3. Initial scaling: using the most recent pair (index m-1)
    # gamma = (s_last^T y_last) / (y_last^T y_last)
    gamma = np.dot(S[-1], Y[-1]) / np.dot(Y[-1], Y[-1])
    r = gamma * q
    
    # 4. Forward loop: oldest history (0) up to newest (m-1)
    for i in range(m):
        beta = rhos[i] * np.dot(Y[i], r)
        r = r + S[i] * (alphas[i] - beta)
        
    # 5. Return descent direction (negated result) as a list
    return (-r).tolist()
