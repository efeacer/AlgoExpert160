def bubbleSort(array):
	"""
	Linear pass for n - 1 times: O(n^2)
	"""
	n = len(array) - 1
	while n >= 1:
		i = 0
		while i < n:
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i] #swap
			i += 1
		n -= 1
	return array