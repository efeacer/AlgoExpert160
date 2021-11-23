def longestPeak(array):
    """
    Single pass: O(n)
    """
    n = len(array)
    curr_len = 0
    max_len = 0
    i = 0
    while i < n - 1 and array[i + 1] <= array[i]:
        i += 1
    uphill_old, steady_old = True, False
    while i < n - 1:
        uphill, steady = array[i + 1] > array[i], array[i + 1] == array[i]
        if uphill_old:
            if steady:
                curr_len = 0
            else:
                curr_len += 1
        elif steady_old:
            if uphill:
                curr_len = 1
            else:
                curr_len = 0
        else:  # downhill
            if uphill or steady:
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
                curr_len = 1
            elif curr_len >= 2:
                curr_len += 1
        uphill_old, steady_old = uphill, steady
        i += 1
    if curr_len >= 2 and (not uphill_old and not steady_old):
        if curr_len + 1 > max_len:
            max_len = curr_len + 1
    return max_len








