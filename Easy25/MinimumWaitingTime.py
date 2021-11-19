def minimumWaitingTime(queries):
	"""
	Greedy, Shortest query first: O(nlogn)
	"""
	queries.sort()
	last = 0
	waiting_time = 0
	len_q = len(queries)
	for i in range(len_q - 1):
		q = queries[i]
		last += q
		waiting_time += last
	return waiting_time
