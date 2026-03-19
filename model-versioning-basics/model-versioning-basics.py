def promote_model(models):
    # Sort models based on the priority rules
    # 1. -accuracy (so higher accuracy comes first)
    # 2. latency (so lower latency comes first)
    # 3. timestamp reversed (so later dates come first)
    
    models.sort(key=lambda x: (-x['accuracy'], x['latency'], x['timestamp']), reverse=False)
    
    # Wait! If we use reverse=False:
    # We want highest accuracy first -> use -accuracy
    # We want lowest latency first -> use latency
    # We want latest timestamp first -> use -timestamp (but you can't negate strings)
    
    # EASIER WAY: Sort such that the "BEST" is at the end, or use reverse=True
    best_model = sorted(models, key=lambda x: (
        x['accuracy'],        # Higher is better
        -x['latency'],       # Lower is better (negated so smaller is 'larger')
        x['timestamp']       # Later is better
    ))[-1]
    
    return best_model['name']