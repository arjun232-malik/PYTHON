a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
d = int(input("Enter the fourth number:"))

if(a>b and a>c and a>d):
    print(a,' is greatest number')
elif(b>a and b>c and b>d):
    print(b,' is greatest number')
elif(c>a and c>b and c>d):
    print(c,' is greatest number')
else:
    print(d,' is the greatest number')