n1=int(input())
n2=int(input())
l1=[]
for i in range(1,n1):
    if (n1 % i == 0):
        l1.append(i)
print(l1)
l2=[]
for i in range(1,n2):
    if (n2 % i == 0):
        l2.append(i)
#print(l2)
a=[]
a=list(set(l1) & set(l2))
print(a[len(a)-1])