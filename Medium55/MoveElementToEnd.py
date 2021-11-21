def moveElementToEnd(array, toMove):
	"""
	Visit each element twice: O(n)
	"""
	count = 0
	for n in array:
		if n == toMove:
			count += 1
	i = 0
	for n in array:
		if n != toMove:
			array[i] = n
			i += 1
	while i < len(array):
		array[i] = toMove
		i += 1
	return array
