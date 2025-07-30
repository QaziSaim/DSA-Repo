class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
def first_append(head,new_value):
  if head is None:
    return new_value
  new_node = Node(new_value)
  new_node.next = head
  return new_node

def print_list(head):
  node = head
  while node is not None:
    print(node.data,end=" ")
    node = node.next
if __name__ == "__main__":
  head = Node(10)
  head.next = Node(20)
  head.next.next = Node(30)
  head.next.next.next = Node(40)
  head.next.next.next.next = Node(50)
  print("Before Append")
  print_list(head)
  print("First Append")
  first_node = first_append(head,0)
  print_list(first_node)
