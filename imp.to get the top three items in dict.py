n1=int(input())
n2 = int(input())
d={}
for i in range (n1):
    for j in range(n2):
         t=(input())
         r=eval(input())
         d[t]= r

print(d)
s=sorted(d.values())
print(s)
k=list(d.keys())
c=list(d.values())
n=-1
while(n>-4):
   p=c.index(s[n])
   print(p)
   print(k[p],d.get(k[p]))
   #to get the key by its value
   n=n-1


