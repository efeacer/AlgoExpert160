def binarySearch(array, target):
	"""
	Problem size is halved each iteration: O(logn)
	"""
	l = 0
	r = len(array) - 1
	while l <= r:
		m = (r + l) // 2
		if target == array[m]:
			return m
		elif target < array[m]:
			r = m - 1
		else:
			l = m + 1
	return -1
