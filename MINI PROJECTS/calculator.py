def cal():
      num=float(input("ENTER FIRST OPERANT:"))
      oper=str(input("ENTER THE OPERATOR:"))
      num2=int(input("ENTER SECOND OPERANT:"))

      if(oper=='+'):
        return (num+num2)
      elif(oper=='-'):
        return (num-num2)
      elif(oper=='*'):
        return (num*num2)
      elif(oper=='/' or oper=='%'):
        return (num/num2)
      elif(oper=='^'):
        return (num**num2)
      else:
        print("invalid operator")
      
   
print("BASIC CALCULATOR")
print(cal())
