def twoNumberSum1(array, targetSum):
	"""
	Brute-force solution: O(n^2)
	"""
	for n1 in array:
		for n2 in array:
			if n1 != n2 and n1 + n2 == targetSum:
				return [n1, n2]
	return []

def twoNumberSum2(array, targetSum):
	"""
	Sort and search: O(nlogn)
	"""
	array.sort()
	i = 0
	j = len(array) - 1
	while i < j:
		n1 = array[i]
		n2 = array[j]
		sum = n1 + n2
		if sum == targetSum:
			return [n1, n2]
		elif sum < targetSum:
			i += 1
		else:
			j -= 1
	return []

def twoNumberSum3(array, targetSum):
	"""
	Solution using hash sets: O(n)
	"""
	s = set()
	for n in array:
		s.add(n)
	for n in array:
		if 2 * n != targetSum and targetSum - n in s:
			return [n, targetSum - n]
	return []