from tkinter import *
from tkinter import ttk
from datetime import date
from tkinter import messagebox
STEPS = 0
CALORIES = 0
ACTIVITIES = []
window = Tk()
window.title('Fitness tracker')
l1 = Label(window, text='Fitness Tracker', bg='black', fg='white', font = ('Arial',50,'bold'))
l1.pack(pady =10)
l2 = Label(window, text='Enter Steps', bg='black', fg = 'white', font = ('Arial', 30, 'bold'))
l2.pack()
e1 = Entry(window, bg = 'white',  width= 20, font = ('Arial', 20))
e1.pack()
l3 = Label(window, text='Enter Calories Burned', bg='black', fg = 'white', font = ('Arial', 30, 'bold'))
l3.pack()
e2 = Entry(window, bg = 'white', width= 20, font = ('Arial', 20) )
e2.pack()
l4 = Label(window, text='Select Activity', bg='black', fg = 'white', font = ('Arial', 30, 'bold'))
l4.pack()
values = ['yoga', 'cycling', 'walking', 'running', 'sports', 'swimming', 'weight lifting']
combo = ttk.Combobox(window, values=values, state='readonly', font = ('Arial', 20))
combo.pack()
def showlog():
  global STEPS, ACTIVITIES, CALORIES
  STEPS += int(e1.get())
  ACTIVITIES.append(combo.get())
  CALORIES += int(e2.get())
  messagebox.showinfo("Info","Activities succesfully logged")
  print(STEPS, CALORIES, ACTIVITIES)
b1 = Button(window, text='Log Activity', command=showlog, font = ('Arial', 20, 'bold'))
b1.pack(pady = 10)
def showdaily():
  dt = date.today()
  unique_activities = set(ACTIVITIES)
  data = ''
  for i in unique_activities:
    data += f"{i} : {ACTIVITIES.count(i)}\n"
  message =  f'Daily summary {dt}: \n -Steps: {STEPS} \n -Calories Burned {CALORIES} \n -Activities: \n  -{data}'
  messagebox.showinfo('Info', message)
b2 = Button(window, text= 'show daily summary', command=showdaily, font = ('Arial',20, 'bold'))
b2.pack(pady =10)
window.mainloop()