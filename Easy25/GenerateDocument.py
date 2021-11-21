def generateDocument(characters, document):
	"""
	Using hash map: O(n)
	"""
	freqs = {}
	for c in characters:
		if c in freqs:
			freqs[c] += 1
		else:
			freqs[c] = 1
	for c in document:
		if not c in freqs or freqs[c] == 0:
			return False
		freqs[c] -= 1
	return True
