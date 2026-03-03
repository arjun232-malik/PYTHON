class ComplexNum:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNum(self):
        print(self.real,"i +",self.img,"j")

    # def __add__(self,num2): # __add__ -->> DUNDER FUNCTION
    #     newReal=self.real+num2.real
    #     newImg=self.img+num2.img
    #     return ComplexNum(newReal,newImg)
    
    def __sub__(self,num2): # __add__ -->> DUNDER FUNCTION
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return ComplexNum(newReal,newImg)

num1=ComplexNum(3,2)
num1.showNum()

num2=ComplexNum(5,7)
num2.showNum()

num3=num1-num2
num3.showNum()
