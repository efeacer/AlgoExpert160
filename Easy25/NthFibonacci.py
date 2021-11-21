def getNthFib(n):
	"""
	Cumulative computation with a single loop: O(n)
	"""
	if n == 1:
		return 0
	f_older = 0
	f_old = 1
	for i in range(n - 2):
		f_new = f_old + f_older
		f_older = f_old
		f_old = f_new
	return f_old