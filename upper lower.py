a=input("enter a string")
c=len(a)
d=0
f=0
for i in range(0,c):
  if a[i]>='A' and a[i]<='Z':
     d=d+1
  else:
     f=f+1
if(d==f):
    print(a.lower())
else:
    print(a.upper())

