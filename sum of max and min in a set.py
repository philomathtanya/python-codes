n=int(input())
s=set()
for i in range (n):
    t=int(input())
    s.add(t)
m=max(s)
n=min(s)
print("sum is",m+n)
