from tkinter import *
window = Tk()
def show():
  selected = []
  if c1.get():
    selected.append('Python')
  if c2.get():
    selected.append('c++')
  l.config(text = selected)
l = Label(window, text = "")
l.pack()
c1 = IntVar()
c2 = IntVar()

box = Checkbutton(window, text='Python', variable=c1,command=show)
box2 = Checkbutton(window, text='c++', variable=c2,command=show)
box.pack()
box2.pack()
window.mainloop()