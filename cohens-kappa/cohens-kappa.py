import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    rater1 = np.asarray(rater1)
    rater2 = np.asarray(rater2)
    n = len(rater1)
    
    # 1. Observed Agreement (p_o)
    # Count how many times the raters agree and divide by total samples
    p_o = np.sum(rater1 == rater2) / n
    
    # 2. Expected Agreement (p_e)
    # Find all unique labels present in both sets
    labels = np.unique(np.concatenate([rater1, rater2]))
    p_e = 0
    for k in labels:
        # (count of label k in rater1 / n) * (count of label k in rater2 / n)
        count1 = np.sum(rater1 == k)
        count2 = np.sum(rater2 == k)
        p_e += (count1 / n) * (count2 / n)
        
    # 3. Handle the degenerate case
    # If p_e is 1.0, the denominator (1 - p_e) becomes 0
    if np.isclose(p_e, 1.0):
        return 1.0
        
    # 4. Calculate Kappa
    kappa = (p_o - p_e) / (1 - p_e)
    
    return float(kappa)