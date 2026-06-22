# linkedlist is a type of linear data structure of consists of nodes with some sort of data and a pointer, or link to next node 

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
'''n1= Node(15)
n2 = Node(1) 
n3 = Node(64)
n1.next = n2
n2.next = n3

print(n1.data)
print(n1.next.data)
print(n1.next.next.data)'''

class Linkedlist:
  def __init__(self):
    self.head = None
  def insert_at_begin(self, value):
    newnode = Node(value)
    if self.head is None:
      self.head = newnode
      return 
    newnode.next = self.head
    self.head = newnode
  def insert_at_end(self, value):
    newnode = Node(value)
    if self.head is  None:
      self.head = newnode
      return
    current = self.head
    while current.next is not None:
      current = current.next
    current.next = newnode
  def get_len(self):
    current = self.head 
    count = 0
    while current is not None:
      current = current.next
      count+=1
    return count
  def insert_at(self, value, index):
    if index < 0 or index > self.get_len():
      print("Index is out of range")
    if index == 0:
      self.insert_at_begin(value)
      return
    newnode = Node(value)
    current = self.head
    for i in range(index-1):
      current = current.next
    newnode.next = current.next
    current.next = newnode
  def display(self):
    current = self.head
    while current is not None:
      print(current.data, end = "->")
      current = current.next
    print("None")


l = Linkedlist()
l.insert_at_begin(52)
l.display()
l.insert_at_begin(21)
l.display()
l.insert_at_end(71)
l.display()
l.insert_at(522,2)
l.display()



    