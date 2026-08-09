def check_for_line():
    word="python"
    line=1
    data=True
    with open("practice.txt","r") as f:
        
        while(data):
         data=f.readline() # data ---->>> string
         if(word in data):
             return line
         line+=1
    return -1     

print(check_for_line())
    