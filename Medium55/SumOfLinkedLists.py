# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
	"""
	O(max(n, m))
	"""
	n1 = linkedListOne
	n2 = linkedListTwo
	carry = 0
	sentinel = LinkedList(-1)
	curr = sentinel
	while n1 and n2:
		sum_ = n1.value + n2.value + carry
		if sum_ > 9:
			sum_ -= 10
			carry = 1
		else:
			carry = 0
		curr.next = LinkedList(sum_)
		n1 = n1.next
		n2 = n2.next
		curr = curr.next
	while n1:
		sum_ = n1.value + carry
		if sum_ > 9:
			sum_ -= 10
			carry = 1
		else:
			carry = 0
		curr.next = LinkedList(sum_)
		n1 = n1.next
		curr = curr.next
	while n2:
		sum_ = n2.value + carry
		if sum_ > 9:
			sum_ -= 10
			carry = 1
		else:
			carry = 0
		curr.next = LinkedList(sum_)
		n2 = n2.next
		curr = curr.next
	if carry > 0:
		curr.next = LinkedList(1)
    return sentinel.next
