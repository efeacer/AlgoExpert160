def smallestDifference(arrayOne, arrayTwo):
    """
    Sorts and binary search on second array for eacg item of the first array: O(nlogn + mlogm + nlogm)
    """
	arrayOne.sort()
	arrayTwo.sort()
	closest_pair = [arrayOne[0], arrayTwo[0]]
	for n1 in arrayOne:
		l = 0
		r = len(arrayTwo) - 1
		closest = arrayTwo[0]
		while l < r:
			m = (l + r) // 2
			mid = arrayTwo[m]
			if abs(n1 - mid) < abs(n1 - closest):
				closest = mid
			if n1 == arrayTwo[m]:
				return [n1, n1]
			elif n1 < arrayTwo[m]:
				r = m - 1
			else:
				l = m + 1
		mid = arrayTwo[l]
		if abs(n1 - mid) < abs(n1 - closest):
			closest = mid
		if abs(n1 - closest) < abs(closest_pair[0] - closest_pair[1]):
			closest_pair = [n1, closest]
	return closest_pair