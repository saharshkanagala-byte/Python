from tkinter import *
window = Tk()
window.title('Radio button example')
l = Label(window, text='Select a language:')
l.pack(anchor='w')
languagevar = StringVar()
languagevar.set('Java') # default selection
rb1=Radiobutton(window, text='Python', variable=languagevar, value = 'Python')
rb1.pack(anchor='w')
rb2=Radiobutton(window, text='Java', variable=languagevar, value = 'Java')
rb2.pack(anchor='w')
rb3=Radiobutton(window, text='C++', variable=languagevar, value = 'C++')
rb3.pack(anchor='w')
rb4=Radiobutton(window, text='Javascript', variable=languagevar, value = 'Javascript')
rb4.pack(anchor='w')
def submit():
  selected = languagevar.get()
  result.config(text=f"you selected: {selected}")
submit = Button(window, text='submit', command=submit)
submit.pack(anchor='w')
result = Label(window)
result.pack(anchor='w')

window.mainloop()
