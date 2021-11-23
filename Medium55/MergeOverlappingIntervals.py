def mergeOverlappingIntervals(intervals):
    """
	Sort and populate stack: O(nlogn)
	"""
	intervals.sort(key=lambda x: (x[0], x[1]))
	n = len(intervals)
	merged_intervals = [intervals[0]]
	i = 1
	while i < n:
		last = merged_intervals.pop()
		curr = intervals[i]
		if curr[0] <= last[1]:
			merged_intervals.append([last[0], max(last[1], curr[1])])
		else:
			merged_intervals.append(last)
			merged_intervals.append(curr)
		i += 1
	return merged_intervals