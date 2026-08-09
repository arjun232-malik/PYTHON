def cal_sum(n):
    if(n==0): # Base case #
        return 0
    else:
        return cal_sum(n-1) + n 

print(cal_sum(5))