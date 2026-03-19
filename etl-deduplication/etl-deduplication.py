def deduplicate(records, key_columns, strategy):
    groups = {}
    order = []
    
    for rec in records:
        # Use a tuple as the dict key for multiple columns
        val_key = tuple(rec[k] for k in key_columns)
        if val_key not in groups:
            order.append(val_key)
            groups[val_key] = []
        groups[val_key].append(rec)
        
    output = []
    for val_key in order:
        group = groups[val_key]
        if strategy == "first":
            output.append(group[0])
        elif strategy == "last":
            output.append(group[-1])
        elif strategy == "most_complete":
            # Helper to count None values in a dict
            def count_none(r):
                return sum(1 for v in r.values() if v is None)
            
            # min() in Python is stable; it picks the first one encountered in a tie
            best_rec = min(group, key=count_none)
            output.append(best_rec)
            
    return output