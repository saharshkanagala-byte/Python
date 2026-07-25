
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      return
    current = self.head
    while current.next is not None:
      current = current.next
    current.next = new_node
  def display(self):
    current = self.head
    print("Linkedlist: ")
    while current is not None:
      print(current.data, end=' ')
      current = current.next
    print()
  def delete_node(self, value):

    if self.head is None:
      print("List is empty")
    if self.head.data == value:
      self.head = self.head.next
      return
    previous = None
    current = self.head
    while current is not None and current.data != value:
      previous = current
      current = current.next
    if current is None:
      print("Value not in list")
      return
def main():
  list = LinkedList()
  while True:
    print('\n 1. append node')
    print('2. dispaly')
    print('3. delete node')
    print('4. exit')

    choice = input('Choice: ')

    if choice == '1':
      value = input('Enter a value')
      list.append(value)
    elif choice == '2':
      list.display()
    elif choice == '3':
      value = input('Enter a value to delete a node')
      list.delete_node(value)
    else:
      break 

main()

    
