def arrayOfProducts(array):
	"""
	Linear computations: O(n)
	"""
	products_before = [1]
	products_after = [1]
	i = 1
	n = len(array)
	while i < n:
		temp = products_before[i - 1]
		products_before.append(temp * array[i - 1])
		products_after.append(1)
		i += 1
	i -= 1
	while i > 0:
		temp = products_after[i]
		products_after[i - 1] = temp * array[i]
		i -= 1
	products = []
	while i < n:
		products.append(products_before[i] * products_after[i])
		i += 1
	return products