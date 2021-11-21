def threeNumberSum(array, targetSum):
	"""
	Check set for each ordered pair: O(n^2)
	"""
	res = []
	s = set()
	for n in array:
		s.add(n)
	array.sort()
	for i in range(len(array)):
		for j in range(i + 1, len(array)):
			n1 = array[i]
			n2 = array[j]
			n3 = targetSum - n1 - n2
			if n3 > n2 and n3 in s:
				res.append([n1, n2, n3])
	return res