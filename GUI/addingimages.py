from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title('Mountains')
image = ImageTk.PhotoImage(Image.open('GUI/imagesforpython.jpeg').resize((400,500)))
imagel = Label(window, image = image)
imagel.pack()
window.mainloop()