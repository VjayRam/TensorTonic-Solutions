def baseline_predict(ratings_matrix, target_pairs):
    """
    Compute baseline predictions using global mean and user/item biases.
    """
    # 1. Calculate Global Mean (mu)
    all_ratings = [r for row in ratings_matrix for r in row if r > 0]
    if not all_ratings:
        return [0.0] * len(target_pairs)
    
    mu = sum(all_ratings) / len(all_ratings)
    
    # 2. Calculate User Biases (b_u)
    user_biases = []
    for row in ratings_matrix:
        rated = [r for r in row if r > 0]
        # Bias = (User Mean) - Global Mean
        bias = (sum(rated) / len(rated)) - mu if rated else 0.0
        user_biases.append(bias)
        
    # 3. Calculate Item Biases (b_i)
    item_biases = []
    num_items = len(ratings_matrix[0])
    for j in range(num_items):
        # Extract column j and filter zeros
        column_rated = [ratings_matrix[i][j] for i in range(len(ratings_matrix)) if ratings_matrix[i][j] > 0]
        # Bias = (Item Mean) - Global Mean
        bias = (sum(column_rated) / len(column_rated)) - mu if column_rated else 0.0
        item_biases.append(bias)
        
    # 4. Compute predictions for target pairs
    predictions = []
    for u, i in target_pairs:
        # Formula: r_ui = mu + b_u + b_i
        pred = mu + user_biases[u] + item_biases[i]
        predictions.append(float(pred))
        
    return predictions