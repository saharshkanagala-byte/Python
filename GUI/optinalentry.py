from tkinter import *
from tkinter import ttk
window = Tk()
window.title('Optinal Entry')
ages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
l1 = Label(window, text='Select a age, gender, and hobby :')
l1.pack()
dp = ttk.Combobox(window, values=ages, state='readonly' )
dp.pack()
dp.set('Age')
gender = ['male', 'female']
dp2 = ttk.Combobox(window, values=gender, state='readonly' )
dp2.pack()
dp2.set('Gender')
hobby = ['singing', 'running', 'eating', 'walking', 'singing', 'play games']
dp3 = ttk.Combobox(window, values=hobby, state='readonly' )
dp3.set('Hobby')
dp3.pack()
window.mainloop()