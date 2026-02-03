class Car:
     
     def __init__(self):
          self.acc=False
          self.brk=False
          self.clutch=False

     def start(self):
          self.clutch=True # hidden
          self.acc=True # hidden
          print("car started....")
    
car1=Car()
car1.start()
