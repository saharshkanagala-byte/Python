from tkinter import *
from PIL import Image, ImageTk
import random
window = Tk()
window.title('Rolling dice')
dice1 = ImageTk.PhotoImage(Image.open('GUI/dice1.png').resize((200,200)))
dice2 = ImageTk.PhotoImage(Image.open('GUI/dice2.png').resize((200,200)))
dice3 = ImageTk.PhotoImage(Image.open('GUI/dice3.png').resize((200,200)))
dice4 = ImageTk.PhotoImage(Image.open('GUI/dice4.png').resize((200,200)))
dice5 = ImageTk.PhotoImage(Image.open('GUI/dice5.png').resize((200,200)))
dice6 = ImageTk.PhotoImage(Image.open('GUI/dice6.png').resize((200,200)))
dice = [dice1,dice2,dice3,dice4,dice5,dice6]
def roll():
  label1.config(image=random.choice(dice))
  label2.config(image=random.choice(dice))
button = Button(window, text='Roll!', bg='aqua', fg='black', height=2, width=20, command=roll)
button.grid(row=1, column=1, columnspan=2, padx = 10, pady=20)
label1 = Label(window, image=random.choice(dice))
label1.grid(row=2,column=1)
label2 = Label(window, image=random.choice(dice))
label2.grid(row=2,column=2)
window.mainloop()
