def findClosestValueInBst(tree, target):
	"""
	Traverse BST: O(nlogn)
	"""
	closest = None
	node = tree
	while node != None:
		if target == node.value:
			return target
		elif target < node.value:
			if not closest or node.value - target < abs(closest - target):
				closest = node.value
			node = node.left
		else:
			if not closest or target - node.value < abs(closest - target):
				closest = node.value
			node = node.right
	return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None