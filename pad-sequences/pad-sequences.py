import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
      return np.zeros((0, 0), dtype=int)

    if not max_len:
      max_len = max(len(seq) for seq in seqs)

    N = len(seqs)

    res = np.full((N, max_len), pad_value, dtype=int)

    for i, seq in enumerate(seqs):
      seq_len = min(len(seq), max_len)

      res[i, :seq_len] = seq[:seq_len]
    
    return res
    

    