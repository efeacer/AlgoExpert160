def tournamentWinner(competitions, results):
	"""
	Traverse the arrays: O(n)
	"""
	points = {}
	best_point = 0
	leader = ""
	for i, competition in enumerate(competitions):
		winner = competition[1 - results[i]]
		if winner in points:
			points[winner] += 3
		else:
			points[winner] = 3
		if points[winner] > best_point:
			best_point = points[winner]
			leader = winner
	return leader
