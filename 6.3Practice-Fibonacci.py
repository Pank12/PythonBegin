#Basic Fibonacci
def fib(n):
    a,b=0,1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(10)

#Complex one
def fib(n):
    a,b=0,1
    if n <= 0:
        print ("Please provide a valid/Positive number")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(-10)