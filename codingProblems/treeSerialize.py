'''
	Serialize and Deserialize a tree

	class Node:
		def __initt__(self, val, left=None, right=None:
			self.val = val
			self.left = left
			self.right = right

	Into a string and back out of a string
        This is it
'''

class Node:
	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

def serialize(root):
	strng = ""

	children = [root]
	while len(children) != 0 :
		current = children.pop(0)
		if current != None:
			strng += current.val + " "
			children.append(current.left)
			children.append(current.right)
		else :
			strng += "None "

	return strng

def deserialize(strng):
	parents = []
	nodes = strng.split(" ")

	level = 0
	levels = [[]]
	levelLen = 2 ** level

	for node in nodes:
		if len(levels[level]) < levelLen:
			levels[level].append(node)
		else :
			level += 1
			levels.append([])
			levelLen = 2 ** level
			levels[level].append(node)

	for i, l in enumerate(levels):
		for j, node in enumerate(l):
			if levels[i][j] != "None":
				levels[i][j] = Node(levels[i][j])
			else :
				levels[i][j] = None

	for i in range(len(levels) - 2):
		for j, node in enumerate(levels[i]):
			if levels[i][j] != None:
				levels[i][j].left = levels[i + 1][2**j - 1]
				levels[i][j].right = levels[i + 1][2**j]

	return levels[0][0]

node = Node('root', Node('left', Node('left.left')))
print(deserialize(serialize(node)).left.left.val)


