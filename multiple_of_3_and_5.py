def multipleof3and5(num):
    sum = 0
    for i in range(1,num):
        if i%3==0 or i%5==0:
            sum = sum +  i
        
            
    print(sum)
            
num = int(input("enter the maxiumum number for the range"))
multipleof3and5(num)
