from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('Pop up dialouge boxes')
def show_info():
  messagebox.showinfo("Info","This is an information pop-up window")
b1 = Button(window, text= 'Show Info', command= show_info)
b1.pack()
def show_error():
  messagebox.showerror("Error","This is an error pop-up window")
b2 = Button(window, text= 'Show Error', command= show_error)
b2.pack()
def show_warning():
  messagebox.showwarning("Warning","This is an warning pop-up window")
b3 = Button(window, text= 'Show Warning', command= show_warning)
b3.pack()
def ask_question(): 
  response = messagebox.askquestion("Question","Do you like Python?")
  print('Response:', response)
b4 = Button(window, text= 'Ask Question', command= ask_question)
b4.pack()
def ask_yes_no(): 
  response = messagebox.askyesno("Yes/No","Do you want to continue?")
  if response:
    print('User chose yes')
  else:
    print('user chose no')
    window.quit()
b5 = Button(window, text= 'Ask Yes/No', command= ask_yes_no)
b5.pack()
window.mainloop()