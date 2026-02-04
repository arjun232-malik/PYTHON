class Student:
     
     def __init__(self,name,age):
          self.__name=name
          self.age=age   

     def __hello(self):
          return self.__name
               
s1=Student("Siddharth",21)


print(s1.__hello())
print(s1.__name)
