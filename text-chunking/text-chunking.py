def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step = chunk_size - overlap

    chunks = []

    for i in range(0, len(tokens), step):
        current = tokens[i : i + chunk_size]
        chunks.append(current)

        if i + chunk_size >= len(tokens):
            break
        
    return chunks
