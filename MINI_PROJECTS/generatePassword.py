print("GENERATE PASSWORD")
n=int(input("ENTER THE PASSWORD LENGTH:"))
import random
import string 

char=string.digits+string.ascii_letters+string.punctuation
password=" "
for i in range(1,n+1):
    password+=random.choice(char)
    
print(password)    
