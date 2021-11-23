def kadanesAlgorithm(array):
	"""
	Break the chain if a negative number completely diminishes
	the contribution of positive numbers encountered so far: O(n)
	"""
	max_cumulative = array[0]
	cumulative = 0
	for item in array:
		cumulative += item
		if cumulative > max_cumulative:
			max_cumulative = cumulative
		if cumulative < 0:
			cumulative = 0
	return max_cumulative