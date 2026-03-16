def item_cf_predict(user_ratings, item_similarities, target):
    """
    Predict the rating using item-based collaborative filtering.
    """
    num = 0
    den = 0 
    for i, (r, s) in enumerate(zip(user_ratings, item_similarities)):
        if i == target:
            continue

        if r > 0 and s > 0:
            num += s * r
            den += s

    return num / den if den != 0 else 0
            
        