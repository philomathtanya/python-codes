n=int(input())
for i in range(0,n+1):
    a=bin(i)
    d=len(a[2:])
    c=len(bin(n))-2
    print((c-d)*" ",a[2:])