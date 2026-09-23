from tkinter import *
# bmi < 18.5 = under weight
# 18.5 - 29.9 = fit
# anything above is overwieght

window = Tk()
window.title('BMI calculator' )
def show():
  height =scale.get()
  weight = scale1.get()
  bmi = weight / (height * height)
  scale2.set(bmi)
  if bmi < 18.5:
    l5.config(bg='red', text='YOU ARE UNDERWEIGHT')
  elif bmi <= 24.9 and bmi >= 18.5:
    l5.config(bg='green', text='YOU ARE FIT')
  else:  
    l5.config(bg='red', text='YOU ARE OVERWEIGHT')
l1 = Label(window, text='BMI Calculator', font = ('Arial', 50, 'bold'))
l1.pack()
l2 = Label(window, text='Check Height in meters')
l2.pack()
scale = Scale(window, from_=0, to=10, resolution= 0.05, orient= HORIZONTAL)
scale.pack()
l3 = Label(window, text="select wieght in KG's")
l3.pack()
scale1 = Scale(window, from_=0, to=200,resolution=0.05 , orient= HORIZONTAL)
scale1.pack()
b = Button(window, text='Sumbit', command=show)
b.pack()
l4 = Label(window, text='Your Bmi')
scale2 = Scale(window, from_=0, to=200, resolution=0.05, orient= HORIZONTAL)
scale2.pack()
l5 = Label(window, text='')
l5.pack()
window.mainloop()