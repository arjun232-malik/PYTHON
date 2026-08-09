class Student:
     #default constructor
     def __init__(self):
          pass
     
     #parameterized constructor
     def __init__(self,name,age):
          self.name=name
          self.age=age

s1=Student("Siddharth",21)
print(s1.name,s1.age)
s2=Student("Siddhu",20)
print(s1.name,s2.age)

# print(s1.height)

# class Car:
#      color="Red"
#      brand="Porsche"
#      model="carrera"

# s1=Car()
# print(s1.color)
# print(s1.brand)
# print(s1.model)
