from tkinter import *

window = Tk()
window.title('Multiplication table')
window.config(bg = 'Dark blue')
l1 = Label(window , text = 
'Enter a number to see its Table:', bg = 'Orange', font = ('Arial', 20, 'bold'), fg = 'Dark blue')
l1.grid(row=1,column=1)
entry = Entry(window, font = ('Arial', 20, 'bold'))
entry.grid(row=1,column=2, padx=20, pady=20)
def multiply():
  num = int(entry.get())
  data = f"Table of {num}\n"
  for i in range(1,11):
    data += f"{num} * {i} = {i*num}\n"
  l2.config(text = data)
    
    
b = Button(window,text = 'Show multiplication table' ,font = ('Arial', 20, 'bold'), command=multiply)


b.grid(row=1,column=3)
l2 = Label(window , text = 
'', bg = 'Orange', font = ('Arial', 20, 'bold'), fg = 'Dark blue')
l2.grid(row=2, column=2)
window.mainloop()