class Stack:
	def __init__(self, capacity):
		self.capacity = capacity
		self.items = [None] * capacity
		self.num_items = 0
	def is_empty(self):
		return (self.num_items == 0)
	def is_full(self):
		return (self.capacity == self.num_items)
	def push(self, item):
		if self.is_full():
			raise IndexError
		else:
			self.items[self.num_items] = item
			self.num_items += 1
	def pop(self):
		if self.is_empty():
			raise IndexError
		else:
			self.num_items -= 1
			return self.items[self.num_items]
	def peek(self):
		if self.is_empty():
			raise IndexError
		else:
			return self.items[self.num_items - 1]
	def size(self):
		return self.num_items