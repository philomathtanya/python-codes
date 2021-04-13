s=input("enter a string")
l=""
a=s.split()
for i in range(0,len(a)):

    if len(a[i])>len(l):
       l=a[i]
print(l)
for i in range(0,len(a)):

    if len(a[i])<len(l):
       l=a[i]
print(l)

