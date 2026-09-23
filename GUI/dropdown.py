from tkinter import *
from tkinter import ttk
window = Tk()
window.title('Dropdown example')
l = Label(window, text='Choose a day')
l.pack()
days = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dp = ttk.Combobox(window, values = days, state='readonly')
dp.pack()
def show():
  selected = dp.get()
  if selected:
    rl.config(text = f"Your selection is {selected}")
  else:
    rl.config(text='You did not select anything')
b = Button(window, text='Submit', command=show)
b.pack()
rl = Label(window, text='')
rl.pack()
window.mainloop()