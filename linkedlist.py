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
  def delete_at_begin(self):
    if self.head is None:
      print("Linked list is empty")
      return 
    self.head = self.head.next
  def delete_at_end(self):
    if self.head is None:
      print("The list is empty")
      return
    if self.head.next is None:
      self.head = None
    current = self.head
    while current.next.next:
      current = current.next
    current.next = None
  def delete_by_value(self, value):
    if self.head is None:
      print("List is empty")
      return
    if self.head.data == value:
      self.head = self.head.next
      return
    previous = None
    current = self.head
    while current is not None and current.data != value:
      previous = current
      current = current.next
    if current is None:
      print("Value not found")
      return
    previous.next = current.next
  def delete_at_position(self, position):
    if self.head is None:
      print("List is empty")
      return
    if position < 0:
      print("Invalid position")
      return
    if position == 0:
      self.head = self.head.next
      return
    current = self.head
    previous = None
    index = 0
    while current is not None and index < position:
      previous = current 
      current = current.next
      index += 1
    if current is None:
      print("Position out of range")
      return
    previous.next = current.next
l = Linkedlist()
l.insert_at_begin(52)
l.display()
l.insert_at_begin(21)
l.display()
l.insert_at_end(71)
l.display()
l.insert_at(522,2)
l.display()
l.insert_at_end(5125)
l.insert_at_end(6314)
l.insert_at_end(1231)
l.insert_at_end(2341)
l.display()
l.delete_at_begin()
l.display()
l.delete_at_end()
l.display()
l.delete_by_value(71)
l.display()
l.delete_at_position(3)
l.display()


    