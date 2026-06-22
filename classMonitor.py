'''In a school, every student wants to leave the class first after the last session. A teacher gave responsibility to the class monitor to make a list of all the students in order they visit the class in the morning. And after the last session, they should leave the class in the same order ( First in first out ). Create a python program that can help the class monitor in managing the list more smoothly.



HINT:

__init__(self): Initializes a new queue with an empty list self.items to store the queue elements.
enqueue(self, item): Adds a new item to the end of the queue by appending it to the self.items list.
dequeue(self): Removes and returns the first item from the queue. It uses pop(0) to remove the item from the front of the list.
peek(self): Returns the first item in the queue without removing it. It simply accesses the first element of the self.items list.
is_empty(self): Returns True if the queue is empty (i.e., self.items is an empty list), otherwise returns False.
After defining the Queue class, the code creates an instance of Queue called student_queue. It then simulates students entering the class by enqueueing their names using enqueue(). After printing the list of students in the class, it simulates students leaving the class by dequeuing and printing their names in the same order using dequeue().

This program demonstrates how a queue can be used to manage a list of students entering and leaving the class in a FIFO (First In First Out) manner.'''


class Queue:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return len(self.items) == 0
  def enqueue(self, var):
    self.items.append(var)
  def dequeue(self):
    if self.isEmpty():
      return "No elements to remove"
    else:
      return self.items.pop(0)
  def peek(self):
    if self.isEmpty():
      return None
    else:
      return self.items[0]
  def display(self):
    print( self.items)
  
student_queue = Queue()
print("Students in the class:")
student_queue.enqueue('bob')
student_queue.enqueue('alice')
student_queue.enqueue('nihaal')
student_queue.enqueue('jalen')
student_queue.display()
print("Students leaving the class in the same order.")
while student_queue.peek():
  print(student_queue.dequeue())