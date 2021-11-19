def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	"""
	Sort and check: O(nlogn)
	"""
	redShirtSpeeds.sort(reverse=True)
	blueShirtSpeeds.sort(reverse=not fastest)
	ts = 0
	n = len(redShirtSpeeds)
	for i in range(n):
		ts += max(redShirtSpeeds[i], blueShirtSpeeds[i])
	return ts