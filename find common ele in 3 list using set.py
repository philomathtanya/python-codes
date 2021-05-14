n=int(input())
l1=list()
for i in range (n):
    t=int(input())
    l1.append(t)
s1 = set(l1)
n=int(input())
l2=list()
for i in range (n):
    y=int(input())
    l2.append(y)
s2=set(l2)
n = int(input())
l3= list()
for i in range(n):
    z = int(input())
    l3.append(z)
s3= set(l3)
print(s1&s2&s3)



