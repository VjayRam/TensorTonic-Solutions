def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    res = []

    for row in X:
        new_row = list(row)
        d = len(row)

        for i in range(d):
            for j in range(i + 1, d):
                prod = row[i] * row[j]
                new_row.append(prod)
            
        res.append(new_row)

    return res