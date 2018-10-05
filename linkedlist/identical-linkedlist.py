# Check if given linked list are identical.

class Node:
		def __init__(self, data):
			self.data = data
			self.next = None


class LinkedList(Node):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None


	def is_identical(self, first_head, second_head):
		if first_head is None and second_head is None:
			return True

		return (first_head.data == second_head.data) and self.is_identical(first_head.next, second_head.next)


if __name__ == '__main__':
	first_head = LinkedList()
	first_head = Node(1)
	first_head.next = Node(2)
	first_head.next.next = Node(3)

	second_head = LinkedList()
	second_head = Node(1)
	second_head.next = Node(2)
	second_head.next.next = Node(30)

	ll = LinkedList()

	print ll.is_identical(first_head, second_head)

