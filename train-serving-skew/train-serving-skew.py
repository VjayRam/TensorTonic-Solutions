import numpy as np

def detect_skew(train_dist, serving_dist, threshold=0.2, eps=1e-10):
    results = {}
    
    for feature in train_dist:
        # Convert to numpy arrays
        p_train = np.array(train_dist[feature])
        p_serve = np.array(serving_dist[feature])
        
        # Add epsilon to prevent log(0) or division by zero
        p_train_adj = p_train + eps
        p_serve_adj = p_serve + eps
        
        # Vectorized PSI calculation
        psi_value = np.sum((p_serve_adj - p_train_adj) * np.log(p_serve_adj / p_train_adj))
        
        results[feature] = {
            "psi": float(psi_value),
            "skewed": bool(psi_value >= threshold)
        }
        
    return results