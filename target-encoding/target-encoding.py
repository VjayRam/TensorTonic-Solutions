def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    sums = {}
    counts = {}

    for cat, target in zip(categories, targets):
        sums[cat] = sums.get(cat, 0) + target
        counts[cat] = counts.get(cat, 0) + 1
    
    means = {}
    for cat in sums:
        means[cat] = float(sums[cat] / counts[cat])
    
    return [means[cat] for cat in categories]