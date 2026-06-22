#1 = add
#2 = sub
#3 = multiply
#4 = divide
import sys
a = int(input("Enter a number to use the calculator : "))
b  = int(input("Enter a second number to use the calculator : "))


operation = int(input("Select a operation: 1 = add, 2 = subtract, 3 = multiply, 4 = divide :"))
if operation > 4:
  sys.exit("ERROR: The operation input is not between 1-4")

if operation == 1:
  print(a+b)
elif operation == 2:
  print(a-b)
elif operation == 3:
  print(a*b)
elif operation ==4:
  print(a/b)
  
