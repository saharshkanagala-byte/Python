


class Passenger:
  def __init__(self, name):
    self.name = name
    self.next = None

    
class TrainPlatform:
  def __init__(self):
    self.head = None
  def board_at_begin(self, name):
    newnode = Passenger(name)
    if self.head is None:
      self.head = newnode
      return 
    newnode.next = self.head
    self.head = newnode
  def board_at_end(self,name):
    new_node = Passenger(name)

    if self.head is  None:
      self.head = new_node
      return
    current = self.head
    while current.next is not None:
      current = current.next
    current.next = new_node
  def get_len(self):
    current = self.head
    count = 0
    while current is not None:
      current = current.next
      count += 1
    return count
  def board_at_mid(self, name):
    current = self.head
    new_node = Passenger(name)
    mid = self.get_len() // 2
    if self.head is None:
      self.head = new_node
      return
    for i in range(mid):
      current = current.next
    
    new_node.next = current.next
    current.next = new_node
  def display(self):
    current = self.head
    while current is not None:
      print(current.name, end = "->")
      current = current.next
    print("None")

def main():
  platfrom = TrainPlatform()

  while True:
    print("\n1. Board at beggining")
    print('2. board at middle')
    print("3. board at end")
    print("4. display")
    print("5. exit")

    choice = input("Choose : ")

    if choice == '1':
      name = input("Passenger name: ")
      platfrom.board_at_begin(name)
    elif choice == '2':
      name = input("Passenger name: ")
      platfrom.board_at_mid(name)
    elif choice == '3':
      name = input("Passenger name: ")
      platfrom.board_at_end(name)
    elif choice == '4':
      platfrom.display()
    else:
      break


main()

    

    
  



