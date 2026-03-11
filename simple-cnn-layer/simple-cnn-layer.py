import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    # Write code here
    x = np.array(x)
    N, Cin, H, W_in = x.shape
    Cout, Cin, KH, KW = W.shape

    H_out = H - KH + 1
    W_out = W_in - KW + 1

    y = np.zeros((N, Cout, H_out, W_out)) + b[None, :, None, None]

    for u in range(KH):
        for v in range(KW):
            x_slice = x[:, :, u:u+H_out, v:v+W_out]

            w_slice = W[:, :, u, v]

            y += np.einsum('nciw,oc->noiw', x_slice, w_slice)
    return y