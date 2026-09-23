from tkinter import *

window = Tk()
window.title('Weight conversion calculator')
def show():
  value = float(e1.get())
  grams = value * 1000
  pounds = value * 2.2
  ounces = value * 35.27
  l5.config(text= grams)
  l6.config(text=pounds)
  l7.config(text=ounces)
l1 = Label(window, text='Enter the weight in Kgs')
l1.grid(row=1,column=1)
e1 = Entry(window)
e1.grid(row=1, column=2)


b1 = Button(window, text='Convert', command=show)
b1.grid(row=1, column=3)
l2 = Label(window, text='Grams')
l2.grid(row=2,column=1,columnspan=1)
l3 = Label(window, text='Pounds')
l3.grid(row=2,column=2,columnspan=1)
l4 = Label(window, text='Ounce')
l4.grid(row=2,column=3,columnspan=1)
l5 = Label(window, text="")
l5.grid(row=3, column=1)
l6 = Label(window, text="")
l6.grid(row=3, column=2)
l7 = Label(window, text="")
l7.grid(row=3, column=3)
window.mainloop()