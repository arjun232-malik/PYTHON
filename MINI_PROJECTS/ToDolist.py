ch = ['To Do List:\n','--> Wake up at 6 am\n','--> 10 push up everyday\n','--> Finish one lecture of C++ DSA everyday\n','--> Do revision of notes\n']
lst=str.join(" ",ch)

while True:
    ask=str(input("(S):SHOW THE LIST OR (A):WANT TO ADD SOMETHING OR (D):WANT TO DELETE THE LINE OR (E):TO EXIT\n"))

    if(ask=='S'):
        print(lst)
    elif(ask=='A'):
        ch.append(str(input("")))
        ch.append('\n')
        lst=str.join(" ",ch)
    elif(ask=='D'):
        ch.pop(int(input("ENTER THE NUMBER OF LINE YOU WANT TO DELETE:")))
        lst=str.join(" ",ch)
    elif(ask=='E'):
        print("BYE :)")
        break
    else:
        print("invalid input")
