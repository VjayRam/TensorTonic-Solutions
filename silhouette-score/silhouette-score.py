import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    """
    n_samples = X.shape[0]
    unique_labels = np.unique(labels)
    
    # 1. Compute all-pairs Euclidean distances efficiently using broadcasting
    # (A-B)^2 = A^2 + B^2 - 2AB
    dist_matrix = np.sqrt(np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=2))
    
    s_i = np.zeros(n_samples)
    
    for i in range(n_samples):
        label_i = labels[i]
        
        # a(i): average distance to all other points in the same cluster
        same_cluster_mask = (labels == label_i)
        same_cluster_mask[i] = False  # Exclude the point itself
        
        n_in = np.sum(same_cluster_mask)
        if n_in > 0:
            a_i = np.mean(dist_matrix[i, same_cluster_mask])
        else:
            # If a cluster has only one point, silhouette is typically defined as 0
            a_i = 0
            
        # b(i): min average distance to points in any OTHER cluster
        b_i = float('inf')
        for label_other in unique_labels:
            if label_other == label_i:
                continue
            
            other_cluster_mask = (labels == label_other)
            avg_dist_to_other = np.mean(dist_matrix[i, other_cluster_mask])
            b_i = min(b_i, avg_dist_to_other)
            
        # Silhouette for point i
        if max(a_i, b_i) == 0:
            s_i[i] = 0
        else:
            s_i[i] = (b_i - a_i) / max(a_i, b_i)
            
    return float(np.mean(s_i))