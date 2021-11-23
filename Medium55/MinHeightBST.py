def minHeightBst(array):
    """
    Each node visited once: O(n)
    """
    n = len(array)
    m = (n - 1) // 2
    bst = BST(array[m])
    minHeightBstHelper(array, 0, m - 1, bst)
    minHeightBstHelper(array, m + 1, n - 1, bst)
    return bst

def minHeightBstHelper(array, l, r, bst):
    if l <= r:
        m = (l + r) // 2
        bst.insert(array[m])
        minHeightBstHelper(array, l, m - 1, bst)
        minHeightBstHelper(array, m + 1, r, bst)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)