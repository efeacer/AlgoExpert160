# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    """
    Visits all nodes once: O(n)
    """
    return branchSumsHelper(root, 0)

def branchSumsHelper(node, curr_sum):
    if not node:
        return []
    elif not node.left and not node.right:  # leaf
        return [curr_sum + node.value]
    else:
        left_sums = branchSumsHelper(node.left, curr_sum + node.value)
        right_sums = branchSumsHelper(node.right, curr_sum + node.value)
        return left_sums + right_sums
