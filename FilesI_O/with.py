with open("demo.txt","r") as f: # as -->> alias
    print(f.read())

with open("demo.txt","w") as f: # as -->> alias
    f.write("by Me")