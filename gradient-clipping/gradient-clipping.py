import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g = np.asarray(g)

    g_norm = np.linalg.norm(g)

    if g_norm <= max_norm or g_norm == 0 or max_norm <= 0:
        return g.copy()

    clip_g = g * (max_norm / g_norm)

    return clip_g