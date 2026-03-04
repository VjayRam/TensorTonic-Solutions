import numpy as np

def roc_curve(y_true, y_score):
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    # 1. Sort indices by score descending
    # Use lexsort with y_true as secondary key to handle ties consistently
    desc_indices = np.argsort(y_score)[::-1]
    y_score = y_score[desc_indices]
    y_true = y_true[desc_indices]

    # 2. Find distinct threshold indices
    # We only care about the TPR/FPR when the score changes
    distinct_value_indices = np.where(np.diff(y_score))[0]
    threshold_indices = np.concatenate([distinct_value_indices, [len(y_true) - 1]])

    # 3. Accumulate TPs and FPs
    tps = np.cumsum(y_true)[threshold_indices]
    fps = 1 + threshold_indices - tps # Total elements - TPs = FPs

    # 4. Convert to Rates
    # Note: total_p = tps[-1], total_n = fps[-1]
    thresholds = y_score[threshold_indices]
    tpr = tps / tps[-1]
    fpr = fps / fps[-1]

    # 5. Add the (0,0) point at threshold inf as required
    tpr = np.concatenate([[0], tpr])
    fpr = np.concatenate([[0], fpr])
    thresholds = np.concatenate([[np.inf], thresholds])

    return fpr, tpr, thresholds