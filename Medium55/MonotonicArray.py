def isMonotonic(array):
	"""
	Single pass: O(n)
	"""
	if len(array) < 2:
		return True
	i = 0
	increasing = False
	decreasing = False
	while i < len(array) - 1:
		n1, n2 = array[i], array[i + 1]
		if n1 < n2:
			increasing = True
		elif n1 > n2:
			decreasing = True
		if increasing and decreasing:
			return False
		i += 1
	return True