from tkinter import *
from datetime import datetime 
window = Tk()
window.config(bg = 'light blue')
window.title('Digital clock')
def update():
  t = datetime.now()
  h = t.strftime('%H')
  m = t.strftime('%M')
  s = t.strftime('%S')
  hr = int(h)
  if hr > 12:
    ampm = "PM"
    hr -= 12
    if hr < 10:
      hr = f"0{hr}"
  else:
    ampm = 'AM'
  t = f"{hr} : {m} : {s} {ampm}"
  tl.config(text = t)
  tl.after(1000, update)
tl = Label(window, text = '00', bg = 'yellow', fg = 'green', font = ('Arial', 200, 'bold'))
tl.pack()
update()
window.mainloop()