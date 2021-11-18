def isValidSubsequence(array, sequence):
	"""
	Both lists are traversed once: O(n + m)
	"""
	i = 0 # index to array
	j = 0 # index to sequence
	len_a = len(array)
	len_s = len(sequence)
	while i < len_a:
		if j == len_s:
			return True
		if array[i] == sequence[j]:
			j += 1
		i += 1
	return j == len_s