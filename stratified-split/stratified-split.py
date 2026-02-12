import numpy as np

def stratified_split(X, y, test_size=0.2, rng=None):
    X = np.array(X)
    y = np.array(y)
    
    train_indices = []
    test_indices = []
    
    # 1. Get unique classes
    classes = np.unique(y)
    
    for c in classes:
        # 2. Get indices for this class
        class_indices = np.where(y == c)[0]
        
        # 3. Shuffle indices WITHIN the class
        if rng is not None:
            rng.shuffle(class_indices)
        else:
            np.random.shuffle(class_indices)
            
        # 4. Calculate split
        n_class = len(class_indices)
        n_test = int(round(n_class * test_size))
        
        # Ensure at least one sample in train if possible
        if n_test == n_class and n_class > 0:
            n_test = n_class - 1
            
        # 5. Distribute to test and train
        test_indices.extend(class_indices[:n_test])
        train_indices.extend(class_indices[n_test:])
    
    # 6. CRITICAL: Sort indices to match the reference output format
    # This ensures that even after shuffling within classes, 
    # the returned arrays are ordered correctly.
    train_indices = np.sort(np.array(train_indices))
    test_indices = np.sort(np.array(test_indices))

    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]