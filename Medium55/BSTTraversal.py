# 1, 2, 5, 5, 10, 15, 22
def inOrderTraverse(tree, array):
	if tree:
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
	return array

# 10, 5, 2, 1, 5, 15, 22
def preOrderTraverse(tree, array):
	if tree:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	return array

# 1, 2, 5, 5, 22, 15, 10
def postOrderTraverse(tree, array):
    if tree:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array
