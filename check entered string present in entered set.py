st=input()
n=int(input())
s=set()
for i in range (n):
    t=input()
    s.add(t)
l=list(s)
for i in l:
    if i==st:
        f=1
    else:
        f=0
if (f==1):
    print("yes")
else:
    print("no")







