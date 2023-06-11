def fib(num):
    a,b=0,1
    for i in range(num):
        print(a,end=' ')
        a,b=b,a+b
n=int(input('enter a number to print fibonacii series'))
fib(n)
        
