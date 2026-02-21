print("GUESS THE NUMBER or QUIT(Q)")
print("-----START-----")
import random
temp=random.randint(1,100)
while True:
    num_1=input("ENTER THE NUMBER:")
    if(num_1=='Q'):
        break
    num_1=int(num_1)
    if(num_1<temp):
      print(num_1,"IS SMALLER")
    elif(num_1>temp):
     print(num_1,"IS LARGER")
    else:
     print("CORRECT GUESS")
     break

print("-----GAME OVER-----")
