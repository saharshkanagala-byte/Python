from tkinter import *
from tkinter import colorchooser

window = Tk()
window.title('ColorDialogeBoxExample')
window.geometry('400x400')
def choose_color(): 
  color = colorchooser.askcolor(title='Choose a color')
  print('Chosen Color:', color[1])
  print(color)
  window.config(bg = color[1])
b4 = Button(window, text= 'Choose Color', command= choose_color)
b4.pack()

window.mainloop()