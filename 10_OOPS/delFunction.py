class Student:
     
     def __init__(self,name,age):
          self.name=name
          self.age=age

s1=Student("Siddharth",21)
print(s1)
print(s1.name)
del s1.name
del s1
print(s1)
print(s1.name)