import math
from collections import Counter

def bleu_score(candidate, reference, max_n):
    """
    Compute the BLEU score for a candidate translation.
    """
    # 1. Handle empty candidate case as per requirements
    if not candidate:
        return 0.0

    c_len = len(candidate)
    r_len = len(reference)
    
    # 2. Compute modified n-gram precisions for each order up to max_n
    precisions = []
    for n in range(1, max_n + 1):
        # Extract and count n-grams from candidate
        cand_ngrams = []
        for i in range(len(candidate) - n + 1):
            cand_ngrams.append(tuple(candidate[i:i+n]))
        
        cand_counts = Counter(cand_ngrams)
        total_cand_ngrams = sum(cand_counts.values())
        
        # If no n-grams of this order exist, the precision is 0
        if total_cand_ngrams == 0:
            return 0.0
            
        # Extract and count n-grams from reference
        ref_ngrams = []
        for i in range(len(reference) - n + 1):
            ref_ngrams.append(tuple(reference[i:i+n]))
        ref_counts = Counter(ref_ngrams)
        
        # Calculate clipped counts: sum(min(count_in_cand, count_in_ref))
        clipped_sum = 0
        for ngram, count in cand_counts.items():
            clipped_sum += min(count, ref_counts.get(ngram, 0))
        
        # Modified precision p_n
        p_n = clipped_sum / total_cand_ngrams
        
        # If any precision is zero, the final BLEU score is 0.0
        if p_n == 0:
            return 0.0
        
        precisions.append(p_n)

    # 3. Calculate the Brevity Penalty (BP)
    if c_len > r_len:
        bp = 1.0
    else:
        bp = math.exp(1 - r_len / c_len)

    # 4. Combine precisions using the Geometric Mean
    # Geometric Mean = exp( (1/N) * sum(log(p_n)) )
    log_sum = sum(math.log(p) for p in precisions)
    geo_mean = math.exp(log_sum / max_n)

    return bp * geo_mean