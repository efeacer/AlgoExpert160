# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    return validateBstHelper(tree, -float('inf'), float('inf'))

def validateBstHelper(tree, min_, max_):
	"""
	Traverse each node once: O(n)
	"""
	if not tree:
		return True
	v = tree.value
	return min_ <= v and v < max_ and validateBstHelper(tree.left, min_, v) and validateBstHelper(tree.right, v, max_)
