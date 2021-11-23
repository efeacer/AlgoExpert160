def firstDuplicateValue(array):
    """
    Very clever mapping, no need to use any data structures: O(n)
    """
    for i, item in enumerate(array):
        if array[abs(item) - 1] < 0:
            return abs(item)
        array[abs(item) - 1] *= -1
    return -1
