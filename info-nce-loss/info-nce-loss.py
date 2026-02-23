import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    Z1 = np.array(Z1)
    Z2 = np.array(Z2)

    S = (Z1 @ Z2.T) / temperature

    logits_max = np.max(S, axis=1, keepdims=True)
    S_stable = S - logits_max

    positives = np.diag(S_stable)

    log_sum_exp = np.log(np.sum(np.exp(S_stable), axis=1))

    loss = -np.mean(positives - log_sum_exp)

    return loss

    