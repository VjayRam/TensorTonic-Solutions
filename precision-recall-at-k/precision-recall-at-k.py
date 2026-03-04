def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    num_count = 0
    for i in recommended[:k]:
       if i in relevant:
           num_count += 1
    precision_k = float(num_count / k)
    recall_k = float(num_count / len(relevant))

    return [precision_k, recall_k]