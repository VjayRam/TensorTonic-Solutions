import numpy as np

def mean_average_precision(y_true_list, y_score_list, k=None):
    """
    Compute Mean Average Precision (mAP) for multiple retrieval queries.
    """
    ap_per_query = []

    for y_true, y_score in zip(y_true_list, y_score_list):
        y_true = np.array(y_true)
        y_score = np.array(y_score)
        
        # 1. Sort labels by score in descending order
        desc_indices = np.argsort(y_score)[::-1]
        y_true_sorted = y_true[desc_indices]
        
        # 2. Apply cutoff k if provided
        if k is not None:
            y_true_sorted = y_true_sorted[:k]
        
        # 3. Calculate Precision at each rank
        # Number of relevant items found up to each rank
        relevant_counts = np.cumsum(y_true_sorted)
        # Total items at each rank (1, 2, 3...)
        ranks = np.arange(1, len(y_true_sorted) + 1)
        precisions = relevant_counts / ranks
        
        # 4. Average Precision is the mean of precisions at relevant ranks
        num_relevant_total = np.sum(y_true) # Total relevant items in ground truth
        
        if num_relevant_total == 0:
            ap = 0.0
        else:
            # We only sum precision where the sorted label is 1
            ap = np.sum(precisions * y_true_sorted) / num_relevant_total
            
        ap_per_query.append(float(ap))

    # 5. Mean Average Precision across all queries
    map_value = float(np.mean(ap_per_query))
    
    return map_value, ap_per_query