def fib(t):
    t1=0
    t2=1
    while(t>0):
        print(t1)
        c=t1+t2
        t1=t2
        t2=c
        t=t-1







n=int(input())
print(fib(n))