def firstNonRepeatingCharacter(string):
	"""
	Using hash map: O(n)
	"""
	freqs = {}
	for c in string:
		if c in freqs:
			freqs[c] += 1
		else:
			freqs[c] = 1
	for i, c in enumerate(string):
		if freqs[c] == 1:
			return i
	return -1
