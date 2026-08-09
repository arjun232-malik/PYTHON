def check_for_word():
   word="learning"
   with open("practice.txt","r") as f:

    data=f.read() # data ---->>> string
    # if(data.find(word)!=-1):
    if(word in data):
       print("Found")
    else:
      print("Not Found")

check_for_word()      