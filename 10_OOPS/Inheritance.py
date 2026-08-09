# class Car:
   
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped") 

# class Porsche(Car):
#     def __init__(self,brand):
#         self.brand=brand    
# p1=Porsche("Carrera")          

# class Carrera(Porsche):
#     def __init__(self, type):
#         self.type=type
# c1=Carrera("Diesel")

# print(c1.type)
# print(c1.start())
# print(p1.brand)

class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"    
class C(A,B):
    varC="welcome to class C"    
c1=C()

print(c1.varA)
print(c1.varB)
print(c1.varC)