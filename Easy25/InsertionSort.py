def insertionSort(array):
	"""
	Linear pass for (n - 1) items: O(n^2)
	"""
	i = 1
	while i < len(array):
		temp = array[i]
		j = i
		while j > 0 and temp < array[j - 1]:
			array[j] = array[j - 1]
			j -= 1
		array[j] = temp
		i += 1
	return array
