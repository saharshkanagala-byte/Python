'''Sindhu attends online classes. She is unable to complete after class assignments Sometimes she misses the due date and then that assignment gets marked as turned in late. She is unable to think how to manage assignments. To help her, write a python program and create a queue data structure so that she can enqueue ( add ) new assignments inside the queue. Also, create a peek() method which can help her in getting the oldest assignment she added in the queue. Create a dequeue method that can help her in removing the peek() assessment after she completes it. Also, create a method isEmpty() so that she can check whether she left with any assignment or not.



HINT:

__init__(self): Initializes the queue as an empty list.
enqueue(self, assignment): Adds an assignment to the end of the queue.
dequeue(self): Removes and returns the assignment at the front of the queue, if the queue is not empty.
peek(self): Returns the assignment at the front of the queue without removing it, if the queue is not empty.
isEmpty(self): Returns True if the queue is empty, False otherwise.
The code then creates an instance my_queue of the AssignmentQueue class and demonstrates how to enqueue, peek, and dequeue assignments from the queue.'''


class Queue:
  def __init__(self):
    self.queue = []
  def isEmpty(self):
    return len(self.queue) == 0
  def enqueue(self, var):
    self.queue.append(var)
  def dequeue(self):
    if self.isEmpty():
      return "No elements in queue to remove" 
    else:
      return self.queue.pop(0)
  def peek(self):
    if self.isEmpty():
      return "No element to see"
    else:
      return self.queue[0]
  
A = Queue()
A.enqueue("Math")
A.enqueue("Science")
A.enqueue("English")
print(A.peek())
if A.isEmpty():
  print("No more work")
else:
  print('There are still assainments to do')




