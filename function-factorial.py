def fact(n1):
    f=1
    while(n1>0):
        f=f*n1
        n1=n1-1
    return f



t1=int(input())
t2=int(input())
print (fact(t1))
print (fact(t2))


