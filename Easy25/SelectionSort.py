def selectionSort(array):
    """
    Linear search for minimum (n - 1) times
    """
    i = 0
    while i < len(array) - 1:
        min_idx = i
        j = i + 1
        while j < len(array):
            if array[j] < array[min_idx]:
                min_idx = j
            j += 1
        array[i], array[min_idx] = array[min_idx], array[i]
        i += 1
    return array