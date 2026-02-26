ch="To Do List:\n"
ch=ch+"1. Wake up at 6 am\n"
ch=ch+"2. 10 push up everyday\n"
ch=ch+"3. Finish one lecture of C++ DSA everyday\n"
ch=ch+"4. Do revision of all lectures notes\n"

while True:
    ask=str(input("(S):SHOW THE LIST OR (A):WANT TO SOMETHING OR (E):TO EXIT\n"))

    if(ask=='S'):
        print(ch)
    elif(ask=='A'):
        ch=ch+str(input(""))
    elif(ask=='E'):
        print("BYE :)")
        break
    else:
        print("invalid input")
