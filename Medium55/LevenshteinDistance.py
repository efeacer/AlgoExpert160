def levenshteinDistance(str1, str2):
	"""
	O(nm) classic DP, use two rows and min(n, m) to optimize space
	"""
    v, m = str2, len(str2)
    s, n = str1, len(str1)
    if len(str1) < len(str2):
        v, s = s, v
        m, n = n, m
    dp_prev = [i for i in range(m + 1)]
    dp_curr = [0 for _ in range(m + 1)]
    for i in range(1, n + 1):
        dp_curr[0] = i
        for j in range(1, m + 1):
            dp_curr[j] = min(dp_prev[j - 1] + int(s[i - 1] != v[j - 1]),
                             dp_prev[j] + 1,
                             dp_curr[j - 1] + 1)
        dp_prev = list(dp_curr)
    return dp_prev[m]