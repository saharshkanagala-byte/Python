class Node:
  def __init__(self, name, phone):
    self.name = name
    self.phone = phone
    self.next = None

class Linkedlist:
  def __init__(self):
    self.head = None
  def insert(self, name, phone):
    while True:
      newnode = Node(name)
      if self.head is None:
        self.head = newnode
      current  = self.head
      while current.next is not None:
        current = current.next
      current.next = newnode

      


    


  
