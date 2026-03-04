import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here
    real_scores = np.array(real_scores)
    fake_scores = np.array(fake_scores)

    return float(np.mean(fake_scores) - np.mean(real_scores))
    