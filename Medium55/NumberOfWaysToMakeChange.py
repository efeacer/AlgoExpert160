def numberOfWaysToMakeChange(n, denoms):
	"""
	Dynamic programming: O(nd)
	S = S0 U {c}
	f(n, S) = f(n - c, S) + f(n, S0)
	"""
	dp = [0] * (n + 1)
	dp[0] = 1
	for c in denoms:
		for i in range(c, n + 1):
			dp[i] += dp[i - c]
	return dp[n]