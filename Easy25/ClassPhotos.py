def classPhotos(redShirtHeights, blueShirtHeights):
	"""
	Sort and check: O(nlogn)
	"""
	redShirtHeights.sort()
	blueShirtHeights.sort()
	n = len(redShirtHeights)
	blues_back = True
	reds_back = True
	for i in range(n):
		rh, bh = redShirtHeights[i], blueShirtHeights[i]
		if blues_back and rh >= bh:
			blues_back = False
		if reds_back and bh >= rh:
			reds_back = False
		if not blues_back and not reds_back:
			return False
	return True
