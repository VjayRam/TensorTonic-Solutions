import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    fpr = np.array(fpr)
    tpr = np.array(tpr)

    if len(fpr) != len(tpr) or len(fpr) < 2:
        return 0.0

    d_fpr = np.diff(fpr)

    avg_tpr = (tpr[:-1] + tpr[1:]) / 2.0

    area = np.sum(d_fpr * avg_tpr)

    return float(area)