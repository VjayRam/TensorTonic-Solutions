def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    if n_items == 0:
        return 0.0
        
    # Using a set comprehension to flatten the 2D list and get unique items
    unique_items = {item for sublist in recommendations for item in sublist}
    
    # Calculate coverage: unique items divided by total catalog size
    return len(unique_items) / n_items