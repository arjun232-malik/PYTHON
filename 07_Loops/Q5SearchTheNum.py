num=(1,4,9,16,25,36,49,64,81,100)
i=1
x=25
# while i<=100:
#     i+=1
#     if(num[3]==i):
#         print(num[3])
#         break
#     else:
#         continue

while i<=len(num):
   
    if(num[i]==x):
        print("Found at index:",i)
        break
    else:
        print("Finding")
    i+=1
     