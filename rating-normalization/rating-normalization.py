def rating_normalization(matrix):
    normalized_matrix = []
    
    for row in matrix:
        # Get only the non-zero ratings
        rated_values = [v for v in row if v != 0]
        
        if not rated_values:
            # If no ratings, add a row of zeros (or the original row)
            normalized_matrix.append([float(v) for v in row])
            continue
            
        # Calculate the average for this specific user
        user_mean = sum(rated_values) / len(rated_values)
        
        # Subtract mean from rated items, leave 0s alone
        normalized_row = [
            float(v - user_mean) if v != 0 else 0.0 
            for v in row
        ]
        normalized_matrix.append(normalized_row)
        
    return normalized_matrix