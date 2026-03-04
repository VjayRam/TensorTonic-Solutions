import math

def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    K = len(predictions)
    res = 0
    
    # Use enumerate to get both the index (i) and the probability (p)
    for i, p in enumerate(predictions):
        if i == target:
            # Formula for the correct class
            smoothed_label = (1 - epsilon) + (epsilon / K)
        else:
            # Formula for incorrect classes
            smoothed_label = epsilon / K
            
        # Accumulate the negative log likelihood
        res += -smoothed_label * math.log(p)
        
    return res