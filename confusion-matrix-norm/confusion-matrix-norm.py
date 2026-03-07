import numpy as np

def confusion_matrix_norm(y_true, y_pred, num_classes=None, normalize='none'):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    if num_classes is None:
        if y_true.size == 0:
            num_classes = 0 # Or handle based on problem requirement
        else:
            num_classes = max(y_true.max(), y_pred.max()) + 1
    
    # Initialize matrix with zeros if empty, or use bincount
    if y_true.size == 0:
        cm = np.zeros((num_classes, num_classes), dtype=np.int64)
    else:
        indices = y_true * num_classes + y_pred
        cm = np.bincount(indices, minlength=num_classes**2).reshape(num_classes, num_classes)
    
    if normalize == 'none':
        return cm.astype(np.int64) # Ensure int64 for 'none'
        
    # Normalization logic...
    cm = cm.astype(np.float64)
    eps = 1e-15 # To prevent division by zero
    
    if normalize == 'true':
        cm /= (cm.sum(axis=1, keepdims=True) + eps)
    elif normalize == 'pred':
        cm /= (cm.sum(axis=0, keepdims=True) + eps)
    elif normalize == 'all':
        cm /= (cm.sum() + eps)
        
    return cm