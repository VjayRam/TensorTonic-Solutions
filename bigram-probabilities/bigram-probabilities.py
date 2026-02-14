from collections import defaultdict

def bigram_probabilities(tokens):
    """
    Returns: (counts, probs)
      counts: dict mapping (w1, w2) -> integer count
      probs: dict mapping (w1, w2) -> float P(w2 | w1) with add-1 smoothing
    """
    # Your code here
    vocab = sorted(list(set(tokens)))
    n_vocab = len(vocab)

    counts = defaultdict(int)
    unigram_counts = defaultdict(int)

    for i in range(len(tokens) - 1):
        w1, w2 = tokens[i], tokens[i+1]
        counts[(w1, w2)] += 1
        unigram_counts[w1] += 1

    probs = {}
    for w1 in vocab:
        denom = unigram_counts[w1] + n_vocab

        for w2 in vocab:
            numerator = counts.get((w1, w2), 0) + 1
            probs[(w1, w2)] = numerator / denom

    return dict(counts), probs

    
    