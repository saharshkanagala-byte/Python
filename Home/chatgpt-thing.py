from tkinter import *
import random
import time
window = Tk()
list = [
  '4x+12',
  '6x-12',
  '-2x-1',
  '5x-1',
  '-5x+3',
  '-6x+1',
  '5x-102',
]
questions = [
  'Find the slope:',
  'Find the y-interpect'
]

l1 = Label(window, text='ChatGPT thing', fg= 'black', bg='white', font= ('arial', 30, 'bold'))
l1.pack()
l2 = Label(window, text= random.choice(list), fg= 'black', bg='white', font= ('arial', 15, 'bold'))
l2.pack()
l3 = Label(window, text=random.choice(questions), fg= 'black', bg='white', font= ('arial', 15, 'bold'))
l3.pack()
e1 = Entry(window)
e1.pack()
def checkanswer():
  answer = int(e1.get())
  if l2 == '4x+12' and l3 == 'Find the slope:':
    if answer == 4:
      b1.config(bg='green')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))
    else:
      b1.config(bg='red')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))

  if l2 == '6x-12' and l3 == 'Find the slope:':
    if answer == 6:
      b1.config(bg='green')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))
    else:
      b1.config(bg='red')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))

  if l2 == '-2x-1' and l3 == 'Find the slope:':
    if answer == 2:
      b1.config(bg='green')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))
    else:
      b1.config(bg='red')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))

  if l2 == '5x-1' and l3 == 'Find the slope:':
    if answer == 4:
      b1.config(bg='green')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))
    else:
      b1.config(bg='red')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))

  if l2 == '-5x+3' and l3 == 'Find the slope:':
    if answer == -5:
      b1.config(bg='green')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))
    else:
      b1.config(bg='red')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))

  if l2 == '-6x+1' and l3 == 'Find the slope:':
    if answer == -6:
      b1.config(bg='green')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))
    else:
      b1.config(bg='red')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))

  if l2 == '5x-102' and l3 == 'Find the slope:':
    if answer == -6:
      b1.config(bg='green')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))
    else:
      b1.config(bg='red')
      time.sleep(3)
      l2.config(text=random.choice(list))
      l3.config(text=random.choice(questions))
b1 = Button(window, text='Check Answer', command= checkanswer)
b1.pack()
window.mainloop()