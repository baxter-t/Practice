'''
	Binary Search Tree
'''

class Node(object):

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Tree(object):

	def __init__(self, first):
		self.root = Node(first)

	def add(self, new):
		current  = self.root
		previous = self.root
		while current != None:
			previous = current
			if new < current.value:
				current = current.left
			else :
				current = current.right
