class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped") 

class Porsche(Car):
    def __init__(self,name,type):
        self.name=name  
        super().__init__(type)
        super().start()
        
p1=Porsche("Carrera","Diesel")
print(p1.name)
print(p1.type) 