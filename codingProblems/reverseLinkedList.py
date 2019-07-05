# Python program to reverse a linked list  
# Time Complexity : O(n) 
# Space Complexity : O(1) 
  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to reverse the linked list 
    def reverse(self): 
        nodes = []
        current = self.head
        while current != None:
            nodes.append(current)
            current = current.next

        out = nodes.pop()
        self.head = out

        while len(nodes) > 0:
            next = nodes.pop()
            out.next = next
            out = next

        out.next = None

    def reverseInPlace(self):
        prev = None
        current = self.head
        next = current.next

        while next != None:
            current.next = prev
            prev = current
            current = next
            next = current.next

        current.next = prev
        self.head = current
          
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data) 
            temp = temp.next
  
  
# Driver program to test above functions 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 

print("Given Linked List")
llist.printList() 
llist.reverseInPlace() 
print("\nReversed Linked List")
llist.printList() 