class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self, capacity):
		self.capacity = capacity
		self.head = None
		self.num_items = 0
	def is_empty(self):
		return (self.num_items == 0)
	def is_full(self):
		return (self.capacity == self.num_items)
	def push(self, item):
		if self.is_full():
			raise IndexError
		else:
			if self.head == None:
				self.head = Node(item)
				self.num_items += 1
			else:
				nextNode = Node(item)
				nextNode.next = self.head
				self.head = nextNode
				self.num_items += 1
	def pop (self):
		if self.is_empty():
			raise IndexError
		else:
			popNode = self.head
			self.head = self.head.next
			self.num_items -= 1
			return popNode.data
	def peek():
		if self.is_empty():
			raise IndexError
		else:
			return self.head.data
	def size(self):
		return self.num_items