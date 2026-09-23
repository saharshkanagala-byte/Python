from tkinter import *
window = Tk()
window.title('Scrollbar example')
text = Text(window, wrap=NONE)

yscroll = Scrollbar(window)
text.config(yscrollcommand=yscroll.set)

yscroll.config(command=text.yview)
for i in range(101):
  text.insert(END, f"This is line {i+1}\n")
text.grid(row=0, column=0)

yscroll.grid(row=0, column=1,sticky='ns')
window.mainloop()