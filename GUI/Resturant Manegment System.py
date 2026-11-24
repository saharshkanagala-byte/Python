from tkinter import *
import time
import random
from datetime import datetime
window = Tk()
window.geometry('900x800')
window.title('Resturant Manegment System')
fr = Frame(window)
fr.grid(row=1, column=1)
l1 = Label(fr, text='Resturant Manegment System',font = ('Arial',30, 'bold'),fg = '#47bbde')
l1.grid(row=1, column=1, columnspan=4)
def update():
  t = datetime.now()
  t = t.strftime('%a %b %d %H:%M:%S %Y')
  ti.config(text = t)
  ti.after(1000, update)
def opentop():
  top = Toplevel(window)
  top.geometry('400x400')
  top.title('Price List')
  l1 = Label(top, text = 'ITEM', fg = 'black', font = ('arial', 20, 'bold'))
  l1.grid(row = 1, column = 1)
  l2 = Label(top, text = 'PRICE', fg = 'black', font = ('arial', 20, 'bold'))
  l2.grid(row = 1, column =2, pady = 10)
  l3 = Label(top, text = 'Fries Meal', fg = '#47bbde', font = ('arial', 20, 'bold'))
  l3.grid(row=3, column = 1)
  l4 = Label(top, text = 'Lunch Meal', fg = '#47bbde', font = ('arial', 20, 'bold'))
  l4.grid(row=4, column = 1)
  l5 = Label(top, text = 'Burger Meal', fg = '#47bbde', font = ('arial', 20, 'bold'))
  l5.grid(row=5, column = 1)
  l6 = Label(top, text = 'Pizza Meal', fg = '#47bbde', font = ('arial', 20, 'bold'))
  l6.grid(row=6, column = 1)
  l7 = Label(top, text = 'Cheese Burger', fg = '#47bbde', font = ('arial', 20, 'bold'))
  l7.grid(row=7, column = 1)
  l8 = Label(top, text = 25, fg = '#47bbde', font = ('arial', 20, 'bold'))
  l8.grid(row=3, column = 2)
  l9 = Label(top, text = 40, fg = '#47bbde', font = ('arial', 20, 'bold'))
  l9.grid(row=4, column = 2)
  l10 = Label(top, text = 35, fg = '#47bbde', font = ('arial', 20, 'bold'))
  l10.grid(row=5, column = 2)
  l11 = Label(top, text = 50, fg = '#47bbde', font = ('arial', 20, 'bold'))
  l11.grid(row=6, column = 2)
  l12 = Label(top, text = 30, fg = '#47bbde', font = ('arial', 20, 'bold'))
  l12.grid(row=7, column = 2)
  l13 = Label(top, text = 35, fg = '#47bbde', font = ('arial', 20, 'bold'))
  l13.grid(row=8, column = 2)
  l14 = Label(top, text = 'Drinks', fg = '#47bbde', font = ('arial', 20, 'bold'))
  l14.grid(row=8, column = 1)
def total():
  one.delete(0,END)
  ce.delete(0,END)
  tote.delete(0, END)
  txe.delete(0, END)
  drinks = de.get()# * 35
  lunch = lme.get() #* 40
  burger = bme.get()# * 35
  pizza =pze.get()  #* 50
  cheese = cbe.get() #* 30
  fries= fle.get() #* 25
  if drinks == '':
    drinks = 0
  else:
    drinks = int(drinks)
  if lunch == '':
    lunch = 0
  else:
    lunch = int(lunch)
  if burger == '':
    burger = 0
  else:
    burger = int(burger)
  if pizza == "":
    pizza = 0
  else:
    pizza = int(pizza)
  if cheese == '':
    cheese = 0
  else:
    cheese=int(cheese)
  if fries == '':
    fries = 0
  else:
    fries = int(fries)
  order = random.randint(11111,99999)
  one.insert(END, order)
  cost = (drinks * 35) +(lunch * 40) +(burger * 35) + (pizza * 50) + (cheese * 30)  + (fries  * 25) 
  ce.insert(END,f"$ {str(cost)}")
  tax = round(cost * (5/100), 2)
  txe.insert(END, f"$ {str(tax)}")
  total = cost + tax
  tote.insert(END, f'$ {total}')
def reset():
  one.delete(0, END)
  de.delete(0, END)
  fle.delete(0, END)
  ce.delete(0, END)
  lme.delete(0, END)
  bme.delete(0, END)
  txe.delete(0, END)
  pze.delete(0, END)
  cbe.delete(0, END)
  tote.delete(0, END)
def exit():
  window.destroy()
ti = Label(fr, text= '',font = ('Arial',20), fg= '#47bbde')
ti.grid(row=2, column=1, columnspan=4)
onl = Label(fr, text='Order No.', fg = '#47bbde' , font= ('Arial', 20))
onl.grid(row=3, column=1, pady = 10)
one = Entry(fr, bg = '#47bbde', fg = 'black',  font= ('Arial', 20), width= 13)
one.grid(row=3, column=2, pady = 10)
dl = Label(fr, fg = '#47bbde', text='Drinks', font= ('Arial', 20), width= 13)
dl.grid(row = 3, column=3, pady = 10)
de = Entry(fr, bg = '#47bbde', fg = 'black',  font= ('Arial', 20), width= 13)
de.grid(row =3, column=4, pady = 10)
fll = Label(fr, text='Fries Meal', fg = '#47bbde' , font= ('Arial', 20))
fll.grid(row=4, column=1, pady = 10)
fle = Entry(fr, bg = '#47bbde', fg = 'black',  font= ('Arial', 20), width= 13)
fle.grid(row=4, column=2, pady = 10)
cl = Label(fr, fg = '#47bbde', text='cost', font= ('Arial', 20), width= 13)
cl.grid(row = 4, column=3, pady = 10)
ce = Entry(fr, bg = '#47bbde', fg = 'black',  font= ('Arial', 20), width= 13)
ce.grid(row =4, column=4, pady = 10)
lml = Label(fr, text='Lunch Meal', fg = '#47bbde' , font= ('Arial', 20))
lml.grid(row=5, column=1, pady = 10)
lme = Entry(fr, bg = '#47bbde', fg = 'black',  font= ('Arial', 20), width= 13)
lme.grid(row=5, column=2,pady=10)
bml = Label(fr, fg = '#47bbde', text='Burger Meal', font= ('Arial', 20), width= 13)
bml.grid(row = 6, column=1, pady = 10)
bme = Entry(fr, bg = '#47bbde', fg = 'black',  font= ('Arial', 20), width= 13)
bme.grid(row =6, column=2, pady = 10)
txl = Label(fr, fg = '#47bbde', text='Tax', font= ('Arial', 20), width= 13)
txl.grid(row = 6, column=3, pady = 10)
txe = Entry(fr, bg = '#47bbde', fg = 'black',  font= ('Arial', 20), width= 13)
txe.grid(row =6, column=4, pady = 10)
pzl = Label(fr, fg = '#47bbde', text='Pizza Meal', font= ('Arial', 20), width= 13)
pzl.grid(row = 7, column=1, pady = 10)
pze = Entry(fr, bg = '#47bbde', fg = 'black',  font= ('Arial', 20), width= 13)
pze.grid(row =7, column=2, pady = 10)
cbl = Label(fr, fg = '#47bbde', text='Cheese Burger', font= ('Arial', 20), width= 13)
cbl.grid(row = 8, column=1, pady = 10)
cbe = Entry(fr, bg = '#47bbde', fg = 'black',  font= ('Arial', 20), width= 13)
cbe.grid(row =8, column=2, pady = 10)
totl = Label(fr, fg = '#47bbde', text='Total', font= ('Arial', 20), width= 13)
totl.grid(row = 8, column=3, pady = 10)
tote = Entry(fr, bg = '#47bbde', fg = 'black',  font= ('Arial', 20), width= 13)
tote.grid(row =8, column=4, pady = 10)
prib = Button(fr, text='PRICE', fg = 'black',bg = 'green', bd =10, width=8, font= ('arial',18, 'bold'), command = opentop)
prib.grid(row=9, column=1, pady=10)
totb = Button(fr, text='TOTAL', fg = 'black',bg = 'blue', bd =10, width=8, font= ('arial',18, 'bold'), command= total)
totb.grid(row=9, column=2, pady=10)
resb = Button(fr, text='RESET', fg = 'black',bg = 'purple', bd =10, width=8, font= ('arial',18, 'bold'), command= reset)
resb.grid(row=9, column=3, pady=10)
exb = Button(fr, text='EXIT', fg = 'black',bg = 'red', bd =10, width=8, font= ('arial',18, 'bold'), command=exit)
exb.grid(row=9, column=4, pady=10)

update()
window.mainloop()