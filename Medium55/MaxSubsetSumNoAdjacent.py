def maxSubsetSumNoAdjacent(array):
	"""
	Clever DP: O(n)
	"""
	if not array:
		return 0
	n = len(array)
	if n == 1:
		return array[0]
	dp = [0] * n
	dp_nadj = array[0]
	dp_adj = max(dp_nadj, array[1])
	for i in range(2, n):
		dp_new = max(dp_adj, array[i] + dp_nadj)
		dp_nadj = dp_adj
		dp_adj = dp_new
	return dp_adj