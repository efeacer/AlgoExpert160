def numberOfWaysToTraverseGraph(width, height):
	"""
	Classic dp: O(wh)
	"""
    min_dim, max_dim = width, height
	if height < width:
		min_dim, max_dim = height, width
	dp = [1 for _ in range(min_dim)]
	for _ in range(1, max_dim):
		for i in range(1, min_dim):
			dp[i] += dp[i - 1]
	return dp[-1]