def evenFibonacci(num):
    n1 = 1
    n2 = 1
    i = 0
    while i<num:
        temp = n1+n2
        n1 = n2
        n2 = temp
        i = i+1
        if n1%2==0:
            print(n1)
            
        
num = 100

evenFibonacci(num)

        

        
        
