def minNumberOfCoinsForChange(n, denoms):
	"""
	Classic DP: O(nd)
	"""
	dp = [float('inf')] * (n + 1)
	dp[0] = 0
	for c in denoms:
		for i in range(c, n + 1):
			dp[i] = min(dp[i], 1 + dp[i - c])
	return -1 if dp[n] == float('inf') else dp[n]
