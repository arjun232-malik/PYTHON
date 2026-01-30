f=open("demo.txt","r")

data=f.read() # read the entire file
print(data)

line1=f.readline() 
print(line1)

line2=f.readline() # read one line at a time
print(line2)

line3=f.readline()
print(line3)

line4=f.readline()
print(line4)

line5=f.readline()
print(line5)

f.close()