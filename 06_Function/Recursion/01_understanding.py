def show(n):
    if(n==0): # Base case #
        return
    # else:
    print(n,end=" ")
    show(n-1)
    print("END")
       

show(5)