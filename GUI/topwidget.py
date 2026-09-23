from tkinter import *

window = Tk()
window.title('TopWIdget Example')
window.geometry('300x300')
def opentop():
  top = Toplevel(window)
  top.geometry('100x100')
  top.title('Example')
  tl = Label(top, text='This is top window')
  tl.pack()
  tb = Button(top, text='Close',command= top.destroy)
  tb.pack()
b1 = Button(window, text='Open Top', command=opentop)
b1.pack()
window.mainloop()