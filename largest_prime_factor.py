def lpf(num):
    fact = 2
    
    while fact**2 <=num:
        while num%fact == 0:
            num = num/fact
        fact = fact + 1
    if num > 1 :
        return num
    return fact
n = int(input("enter the number"))
print(lpf(n))
