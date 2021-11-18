def nonConstructibleChange(coins):
	"""
	Sort and search: O(nlogn)
	"""
	coins.sort()
	to_change = 1
	i = 0
	while i < len(coins):
		coin = coins[i]
		can_change = (to_change - 1) + coin # max_changed = to_change - 1
		if coin <= to_change and can_change >= to_change: 
			to_change = can_change + 1
			i += 1
		else: # to_change is less then all members of [coin, coin + 1, ..., can_change - 1, can_change]
			return to_change
	return to_change