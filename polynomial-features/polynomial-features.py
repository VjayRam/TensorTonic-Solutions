def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    # Initialize the result list
    result = []
    
    # Iterate through each input value
    for x in values:
        # Generate a row: [x^0, x^1, ..., x^degree]
        # Using x**p in a list comprehension
        row = [x**p for p in range(degree + 1)]
        
        # Add the completed row to our matrix
        result.append(row)
        
    return result
