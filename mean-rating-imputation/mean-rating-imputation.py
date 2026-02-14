def mean_rating_imputation(ratings_matrix, mode):
    num_rows = len(ratings_matrix)
    num_cols = len(ratings_matrix[0]) if num_rows > 0 else 0
    
    # Initialize the result matrix as a copy
    res = [row[:] for row in ratings_matrix]

    if mode == "user":
        for i in range(num_rows):
            # Filter out zeros to find valid ratings for this user
            valid_ratings = [r for r in ratings_matrix[i] if r != 0]
            # Calculate mean (handle case with no ratings)
            user_mean = sum(valid_ratings) / len(valid_ratings) if valid_ratings else 0.0
            
            # Fill missing values in this row
            for j in range(num_cols):
                if res[i][j] == 0:
                    res[i][j] = float(user_mean)

    elif mode == "item":
        for j in range(num_cols):
            # Collect ratings for this item across all users
            valid_ratings = [ratings_matrix[i][j] for i in range(num_rows) if ratings_matrix[i][j] != 0]
            # Calculate mean (handle case with no ratings)
            item_mean = sum(valid_ratings) / len(valid_ratings) if valid_ratings else 0.0
            
            # Fill missing values in this column
            for i in range(num_rows):
                if res[i][j] == 0:
                    res[i][j] = float(item_mean)
                    
    return res