# Remove duplicates from an unsorted linked list
# Write a removeDuplicates() function which takes a list and deletes any duplicate nodes 
# from the list. The list is not sorted.

# Solution using set(hashing technique).
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def removeDuplicates(self):
		s = set()
		curr = prev = self.head

		while curr is not None:
			curr_data = curr.data
			if curr_data in s:
				prev.next = curr.next
				curr = None
			else:
				s.add(curr_data)
				prev = curr

			curr = prev.next

	def printList(self):
		curr = self.head

		while curr is not None:
			print curr.data, 
			curr = curr.next

if __name__ == '__main__':
	ll = LinkedList()
	ll.head = Node(2)
	second = Node(1)
	third = Node(2)
	fourth = Node(4)

	ll.head.next = second
	second.next = third
	third.next = fourth

	print 'Linked List BEFORE removing duplicates!'
	ll.printList()

	print '\n'
	
	print 'Linked List AFTER removing duplicates!'
	ll.removeDuplicates()
	ll.printList()

		