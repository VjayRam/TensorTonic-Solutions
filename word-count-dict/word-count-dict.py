from collections import Counter

def word_count_dict(sentences):
    # 1. Flatten the list of lists into one big list of words
    all_words = []
    for sentence in sentences:
        for word in sentence:
            all_words.append(word)
    
    # 2. Let Counter do the heavy lifting
    counts = Counter(all_words)
    
    # 3. Convert back to a standard dict to match requirements
    return dict(counts)