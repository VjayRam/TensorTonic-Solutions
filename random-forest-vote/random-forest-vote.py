import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    predictions = np.array(predictions)
    num_trees, num_samples = predictions.shape
    final = []

    for i in range(num_samples):
        sample_votes = predictions[:, i]
        classes, counts = np.unique(sample_votes, return_counts = True)
        max_votes = np.max(counts)

        winners = classes[counts == max_votes]

        final.append(int(winners[0]))

    return final