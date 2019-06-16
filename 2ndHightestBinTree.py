'''
	Write a function to find  the 2nd largest element in a binary search tree
'''

class BinaryTreeNode(object):
	
	def __init__(self, value):
		self.value = value
		self.left  = None
		self.right = None

	def insert_left(self, value):
		self.left = BinaryTreeNode(value)
		return self.left

	def insert_right(self, value):
		self.right = BinaryTreeNode(value)
		return self.right

def 2ndHighest(root):
	parent = root
	current = parent.right

	while current.right != None:
		parent = current
		current = current.right
	
	return parent.value
