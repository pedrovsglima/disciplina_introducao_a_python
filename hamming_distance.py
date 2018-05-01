def hamming_distance(a, b):
    result = ['1' for x, y in zip(a, b) if int(x)^int(y)]
    return len(result)
