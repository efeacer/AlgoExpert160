# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
	"""
	Examine each node once: O(n)
	"""
	curr = linkedList
	while curr:
		next = curr.next
		if next and next.value == curr.value:
			curr.next = next.next
		else:
			curr = curr.next
	return linkedList