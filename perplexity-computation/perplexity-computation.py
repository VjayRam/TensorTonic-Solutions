def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    n = len(actual_tokens)
    log_probs_sum = 0

    for i, token_idx in enumerate(actual_tokens):
        p_i = prob_distributions[i][token_idx]
        log_probs_sum += math.log(p_i)

    

    return math.exp(-(log_probs_sum / n))
  
  