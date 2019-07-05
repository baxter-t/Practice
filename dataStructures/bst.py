'''
    Binary Search Tree
'''

class Node(object):

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def visitPrint(root):
    print(root.value)

def traversal(root, visit):
    if root == None:
        return
    else :
        traversal(root.left, visit)
        visit(root)
        traversal(root.right, visit)

class BST(object):

    def __init__(self, first):
        self.root = Node(first)

    def add(self, newOb):
        current = self.root
        previous = current

        while current != None:
            if newOb < current.value:
                current = current.left
                if current == None:
                    previous.left = Node(newOb)
                    return
            elif newOb > current.value:
                current = current.right
                if current == None:
                    previous.right = Node(newOb)
                    return

            previous = current

    def exists(self, element):
        current = self.root
        while current != None:
            if current.value == element:
                return True
            elif element < current.value:
                current = current.left
            else:
                current = current.right
        return False


test = BST(4)
test.add(2)
test.add(5)

traversal(test.root, visitPrint)
print(test.exists(6))


