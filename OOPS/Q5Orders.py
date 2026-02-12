class Order:
     
     def __init__(self,item,price):
          self.item=item
          self.price=price
     
     def __gt__(o2,self):
          return o2.price > self.price

o1=Order("Pen Drive",350)
o2=Order("HeadPhone",1980)

print(o2>o1)
