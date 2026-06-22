#Queue is a linear data structure that follows FiFo(First in First out) 
#Think of a queue as people standing in a line at the supermarket for the checkout, the first person to stand in the line is also the first who can pay and leave the supermarket
'''Basic operations we can do on a queue are:
Enqueue: Adds a new element to the queue.
Dequeue: Removes and returns the first (front) element from the queue.
Peek: Returns the first element in the queue.
isEmpty: Checks if the queue is empty.
Size: Finds the number of elements in the queue.'''

class Queue:
  def __init__(self):
    self.queue = []
  def Is_empty(self):
    return len(self.queue) == 0
  def Enqueue(self, val):
    self.queue.append(val)
  def Dequeue(self):
    if self.Is_empty():
      return "queue is empty"
    else:
      return self.queue.pop(0)
  def Peek(self):
    if self.Is_empty():
      return "queue is empty"
    else:
      return self.queue[0]
  def Size(self):
    return len(self.queue)
  def Display(self):
    for i in self.queue:
      print(i, end=" ")
    print()
a = Queue() 
a.Enqueue(10)
a.Enqueue(12)
a.Enqueue(21)
a.Enqueue(36)
a.Enqueue(76)
a.Enqueue(15)
a.Display()
print(a.Peek())
print(a.Dequeue())
print(a.Peek())
a.Display()