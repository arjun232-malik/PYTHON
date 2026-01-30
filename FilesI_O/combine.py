# f=open("demo.txt","r+") # r+ --->> combine read and write operation

# f=open("demo.txt","w+") # w+ --->>> it truncate the file with combination of read and write operation
# f.write("helllooo")

f=open("demo.txt","a+")
print(f.read())
f.write("helllooo")
f.close()