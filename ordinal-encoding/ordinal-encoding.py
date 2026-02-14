def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    mapping = {category: i for i, category in enumerate(ordering)}

    return [mapping[v] for v in values]