import math

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    res = []
    for i in x:
        if i > 0:
            res.append(float(i))
        else:
            res.append(float(alpha * (math.exp(i) - 1)))
    
    return res
    
