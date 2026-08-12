from tkinter import *

window = Tk()
window.config(bg = 'dark blue' )
window.title('Login page')
l1 = Label(window,text = 'Username' ,bg = 'orange', fg ='yellow')
l1.grid(row=0, column=0)
e = Entry(window)
e.grid(row=0,column=2)
l2 = Label(window, text = 'Password',bg = 'orange', fg ='yellow' )
l2.grid(row=1, column=0)
e2 = Entry(window, show = '*')
e2.grid(row=1,column=2)
b = Button(window, text = 'Sumbit')
b.grid(row = 3, column= 2)

window.mainloop()
