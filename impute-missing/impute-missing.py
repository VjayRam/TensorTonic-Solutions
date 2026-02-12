import numpy as np

def impute_missing(X, strategy='mean'):
    # 1. Always work on a float copy to handle NaNs and upcasting
    X_imputed = np.array(X, copy=True, dtype=float)
    
    # 2. Handle 1D arrays by temporarily treating them as 2D (1 column)
    is_1d = X_imputed.ndim == 1
    if is_1d:
        X_imputed = X_imputed.reshape(-1, 1)
    
    # 3. Iterate over each column
    for col_idx in range(X_imputed.shape[1]):
        column = X_imputed[:, col_idx]
        mask = np.isnan(column)
        observed = column[~mask]
        
        if len(observed) == 0:
            # All-NaN column: requirements say fill with 0
            fill_val = 0.0
        else:
            if strategy == 'mean':
                fill_val = np.mean(observed)
            else:
                fill_val = np.median(observed)
        
        # Fill the NaNs in this column
        X_imputed[mask, col_idx] = fill_val
        
    # 4. Return to original shape if it was 1D
    if is_1d:
        return X_imputed.flatten()
        
    return X_imputed