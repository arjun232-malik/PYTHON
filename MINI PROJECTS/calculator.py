def add():
  num1=float(input("Enter the 1st numbe: "))
  num2=float(input("enter the 2nd nummber: "))
  return num1+num2

def sub():
  num1=float(input("Enter the 1st number: "))
  num2=float(input("enter the 2nd nummber: "))
  return num1-num2

def multiply():
  num1=float(input("Enter the 1st number: "))
  num2=float(input("enter the 2nd nummber: "))
  return num1*num2

def div():
  num1=float(input("Enter the 1st number: "))
  num2=float(input("enter the 2nd nummber: "))
  if num2==0:
    print("Error\n2nd number can't be zero")
  else:
    return num1/num2
                  
def powerOf():
  num1=float(input("Enter the 1st number: "))
  num2=float(input("Enter the 2nd nummber: "))
  return num1**num2
   
print("-----BASIC CALCULATOR-----")

while True:
  choice=int(input("Which operation you want to do :\n1. for addition\n2. for subtraction\n3. for multiplication\n4. for division\n5. for power of\n6. for exit\n"))
   
  if choice==1:
    print(add())
  elif choice==2:
    print(sub())
  elif choice==3:
    print(multiply())
  elif choice==4:
    print(div())
  elif choice==5:
    print(powerOf())
  elif choice==6:
    print("Thank you for using it :)")
    break
  else:
    print("Invalid choice\nMake the correct choice")

