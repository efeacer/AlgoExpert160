# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
		"""
		Visit all once: O(n)
		"""
		if not self:
			return []
		q = []
		q.append(self)
		while q:
			n = q.pop(0)
			array.append(n.name)
			for c in n.children:
				q.append(c)
		return array