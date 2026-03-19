import numpy as np

def entropy_node(y):
    if len(y) == 0:
        return 0.0
    
    # Get counts for each unique class
    _, counts = np.unique(y, return_counts=True)
    
    # Calculate probabilities
    probs = counts / len(y)
    
    # Standard Entropy formula: -sum(p * log2(p))
    # Note: np.unique only returns classes that exist, so p will always be > 0
    entropy = -np.sum(probs * np.log2(probs))
    
    return float(entropy)