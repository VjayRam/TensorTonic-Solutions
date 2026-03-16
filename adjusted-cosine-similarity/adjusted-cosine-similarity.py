import math

def adjusted_cosine_similarity(ratings_matrix, item_i, item_j):
    # 1. Calculate all user means first
    user_means = []
    for row in ratings_matrix:
        rated = [v for v in row if v > 0]
        user_means.append(sum(rated) / len(rated) if rated else 0)

    num = 0
    den_i = 0
    den_j = 0
    
    # 2. Iterate through users to find those who rated both items
    for u in range(len(ratings_matrix)):
        ri = ratings_matrix[u][item_i]
        rj = ratings_matrix[u][item_j]
        
        if ri > 0 and rj > 0:
            mean = user_means[u]
            diff_i = ri - mean
            diff_j = rj - mean
            
            num += diff_i * diff_j
            den_i += diff_i ** 2
            den_j += diff_j ** 2
            
    # 3. Handle division by zero
    denominator = math.sqrt(den_i) * math.sqrt(den_j)
    if denominator == 0:
        return 0.0
        
    return num / denominator