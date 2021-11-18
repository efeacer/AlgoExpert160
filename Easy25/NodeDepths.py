def nodeDepths(root):
    """
    Each node visited once: O(n)
    """
    return nodeDepthsHelper(root, 0)

def nodeDepthsHelper(node, depth):
    if not node:
        return 0
    return depth + nodeDepthsHelper(node.left, depth + 1) + nodeDepthsHelper(node.right, depth + 1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
