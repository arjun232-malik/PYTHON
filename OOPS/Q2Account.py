class Account:
     
     def __init__(self,account_no,balance):
          self.acc=account_no
          self.balance=balance
     
     def debit(self,amount):
          self.balance-=amount
          print(amount," was debited from your account")
          print("Your available balance is ",self.balance)

     def credit(self,amount):
          self.balance+=amount
          print(amount," was credited to your account")
          print("Your available balance is ",self.balance)

     def final_amount(self):
          return self.balance  
    
a1=Account(102577789,1150000)
print("Account number:",a1.acc)
print("Account balance:",a1.balance)
a1.debit(3000)
a1.credit(2500)
print("total amount after credits and debits is ",a1.final_amount())