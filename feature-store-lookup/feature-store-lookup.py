def feature_store_lookup(feature_store, requests, defaults):
    results = []
    
    for req in requests:
        user_id = req['user_id']
        online_features = req['online_features']
        
        # 1. Get offline features (fallback to defaults if user not found)
        offline_features = feature_store.get(user_id, defaults)
        
        # 2. Merge dictionaries 
        # The {**dict1, **dict2} syntax creates a new merged dictionary
        combined = {**offline_features, **online_features}
        
        results.append(combined)
        
    return results