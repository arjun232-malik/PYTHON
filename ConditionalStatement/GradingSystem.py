marks = int(input('Enter the marks: '))

if(marks>=90 and marks<=100):
    print('A Grade')
elif(marks>80 and marks<=89):
    print('B Grade')
elif(marks>70 and marks<=79):
    print('C Grade')   
else:
    print('D Grade')