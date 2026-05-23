# def height(abhay,arjun):
#     diff=arjun-abhay
#     return diff

# print(height(1.75,1.77)) # positional argument


#keyword argument

def height(abhay=1.75,arjun=1.77):
    diff=arjun-abhay
    return diff

def height(arjun=1.77,abhay=1.75):
    diff=arjun-abhay
    return diff