import random
num = random.randint(1,100)


while True:
  user = int(input("Select a number 1-100"))
  if user == num:
    print("You won!")
    break
  elif  user < num:
    print("Higher") 
  elif user > num:
    print("Lower")



