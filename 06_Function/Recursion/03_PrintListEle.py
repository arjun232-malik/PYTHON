# teacher's method
def ele_list2(a,b):
    if(b==len(a)): 
        return
    print(a[b])
    ele_list2(a,b+1)

cities=["Delhi","Noida","Pune","Rajkot","Chennai"]
ele_list2(cities,0)

# My method
#  def ele_list(a,b):
#       if(b==-1):
#          return str(a[0])
#       print(a[b])
#       ele_list(a,b-1)

#  cities=["Delhi","Noida","Pune","Rajkot","Chennai"]
#  ele_list(cities,len(cities)-1)