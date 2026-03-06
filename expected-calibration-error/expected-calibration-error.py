import numpy as np

def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    n = len(y_true)
    
    # Initialize ECE
    ece = 0.0
    
    # Generate bin boundaries
    # Equal-width bins over [0, 1]
    bin_boundaries = np.linspace(0, 1, n_bins + 1)
    
    for i in range(n_bins):
        # Define bin range
        bin_low = bin_boundaries[i]
        bin_high = bin_boundaries[i + 1]
        
        # Find indices of predictions that fall into this bin
        # Edge case: 1.0 goes into the last bin
        if i == n_bins - 1:
            bin_indices = np.where((y_pred >= bin_low) & (y_pred <= bin_high))[0]
        else:
            bin_indices = np.where((y_pred >= bin_low) & (y_pred < bin_high))[0]
            
        # If the bin is not empty, calculate its contribution
        if len(bin_indices) > 0:
            # |Bm| / n
            weight = len(bin_indices) / n
            
            # Confidence: average of predicted probabilities in the bin
            conf_bm = np.mean(y_pred[bin_indices])
            
            # Accuracy: fraction of positive labels in the bin
            acc_bm = np.mean(y_true[bin_indices])
            
            # Add weighted absolute difference to total ECE
            ece += weight * np.abs(acc_bm - conf_bm)
            
    return float(ece)