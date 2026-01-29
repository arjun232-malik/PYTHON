def fac(a=5):
    f=1
    for i in range(1,a+1,1):
        f*=i
    print(f)    
    return f   

fac()