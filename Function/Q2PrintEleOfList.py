 # teacher's method
def ele_list2(a):
    for i in a:
        print(a,end=" ")
    return a

cities=["Delhi","Noida","Pune","Rajkot","Chennai"]
ele_list2(cities)

 # My method
def ele_list(a):
    for i in range(0,len(a),1):
        print(a[i],end=" ")
    return a    

ele_list([7,3,6,5,4,1])
