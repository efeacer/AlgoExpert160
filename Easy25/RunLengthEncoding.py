def runLengthEncoding(string):
	"""
	One pass: O(n)
	"""
	if not string:
		return ""
	res = ""
	old_char = string[0]
	count = 1
	i = 1
	while i < len(string):
		curr_char = string[i]
		if curr_char == old_char:
			count += 1
			if count == 9:
				res += "9" + old_char
				count = 0
		else:
			if count != 0:
				res += str(count) + old_char
			old_char = curr_char
			count = 1
		i += 1
	res += str(count) + old_char
    return res
