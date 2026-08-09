def fac(n):
    if(n==0 or n==1): # Base case #
        return 1
    else:
        return fac(n-1)*n 

print(fac(5))