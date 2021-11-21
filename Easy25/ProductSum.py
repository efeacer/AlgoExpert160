# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
	return productSumHelper(1, array)

def productSumHelper(d, item):
	"""
	Go as deep as you can for each item: O(nd)
	"""
	if item is []:
		return 0
	if type(item) is int:
		return item
	inner_sum = 0
	for inner in item:
		inner_sum += d * productSumHelper(d + 1, inner)
	return inner_sum