


class MagicalLocation:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.next = None
class MahicalTrainRoute:
  def __init__(self):
    self.head = None
  def add_location(self, name, description):
    new_node = MagicalLocation(name, description)
    if self.head is None:
      self.head = new_node
      return
    current = self.head
    while current.next is not None:
      
      current = current.next
    current.next = new_node
  def remove_location(self, name):
    if self.head is None:
      print("List is empty")
      return
    if self.head.name == name:
      self.head = self.head.next
      return
    current = self.head
    previous = None
    while current is not None and current.name != name:
      previous = current
      current = current.next
    if current is None:
      print("Value not in list")
      return
  def display(self):
    current = self.head
    while current is not None:
      print('Location:', current.name)
      print('Description:', current.description)
      current = current.next
    print('---------------------------------')

def main():
  list = MahicalTrainRoute()
  while True:
    print('\n 1. Add location')
    print('2. Delete location')
    print('3. Display')
    print('4.Exit')

    choice = input('Choice: ')
    
    if choice == '1':
      name = input("Enter a name: ")
      description = input('Enter a description: ')
      list.add_location(name, description)
    elif choice == '2':
      name = input("Enter a name to delete: ")
      list.remove_location(name)
    elif choice == '3':
      list.display()
    else:
      break
main()
    

    

  
