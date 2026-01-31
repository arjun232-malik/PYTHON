with open("numbers.txt","r") as f:
    data=f.read()
    print(data)
    count=0
    num=data.split(",")
    for val in num:
        if(int(val)%2==0):
            count+=1
    print(count)        

    # num=""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         int(num)
    #         if(int(num)%2==0):
    #             count+=1
    #         num=""
    #     else:
    #         num+=data[i]