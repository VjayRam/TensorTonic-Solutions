import math

def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    res = []

    for val in values:
        theta = ((2 * math.pi * val) / period)
        encoding = [math.sin(theta), math.cos(theta)]
        res.append(encoding)
    
    return res