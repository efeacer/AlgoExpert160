def hasSingleCycle(array):
    """
    Single loop: O(n)
    """
    n = len(array)
    i = 0
    node = 0
    while i < n:
        if i != 0 and node == 0:
            return False
        node = (node + array[node]) % n
        i += 1
    return node == 0
