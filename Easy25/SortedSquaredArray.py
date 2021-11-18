def sortedSquaredArray(array):
	"""
	Split the array to negatives and positives, then merge: O(n)
	"""
	negatives = []
	positives = []
	i = 0
	while i < len(array) and array[i] < 0:
		negatives.append(array[i])
		i += 1
	while i < len(array):
		positives.append(array[i])
		i += 1
	j = len(negatives) - 1 # index to negatives
	k = 0 # index to positives
	squares = []
	while j >= 0 and k < len(positives):
		square_n = negatives[j] ** 2
		square_p = positives[k] ** 2
		if square_n <= square_p:
			squares.append(square_n)
			j -= 1
		else:
			squares.append(square_p)
			k += 1
	while j >= 0:
		squares.append(negatives[j] ** 2)
		j -= 1
	while k < len(positives):
		squares.append(positives[k] ** 2)
		k += 1
	return squares
