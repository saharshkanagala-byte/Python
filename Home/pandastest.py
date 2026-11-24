import pandas as pd
name =''
shift = ''
index = ''
dept = ''
employees = pd.DataFrame(columns = ['Name', 'Shift', 'Dept'])
employees.loc[len(employees)] = {'Name':'Employee1', 'Shift': 'Afternoon', 'Dept':'HR'}
def addEmployee():
  name = input("Enter the employee's name:")
  shift = input("Enter the employee's shift")
  employees.loc[len(employees)] = {'Name':name,'Shift':shift}
def insertAtIndex():
  name = input("Enter the employee's name:")
  shift = input("Enter the employee's shift")
  index = int(input('Enter a index:'))
  employees.iloc[index] = {'Name':name,'Shift':shift}
def addDeptColumn():
  dept = input('Enter the dept:')
  employees.loc[len(employees)] = {'Dept':dept}
def removeEmployees():
  global employees
  name = input('Enter employee to remove:')
  length = len(employees)
  employees = employees[employees['name'] != name]
  if len(employees) < length:
    print(f"All records for {name} have been removed")
  else:
    print(f'Employee not in records with the name {name}')
def display():
  print('/nCurrent List')
  print(employees)
while True:
  print('1. Add employee, 2. Insert At Index, 3.Add dept column, 4. remove employees, 5. display, 6. exit')
  userinput = input('Enter a choice')
  if userinput.isdigit():
    userchoice = int(userinput)
  else:
    print('Invalid input')
  if userchoice == 1:
    addEmployee()
  elif userchoice == 2:
    insertAtIndex()
  elif userchoice ==3:
    addDeptColumn()
  elif userchoice == 5:
    display()
  elif userchoice ==6:
    print('Bye')
    break
  else:
    print('Invalid Choice')