class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

def printlist(head):
  node = head
  while head is not None:
    print(head.data,end=" ")
    head = head.next
if __name__== "__main__":
  head = Node(10)
  head.next = Node(20)
  head.next.next = Node(30)
  head.next.next.next = Node(50)
  print("Printing The Entire Linked List")
  printlist(head)
  
