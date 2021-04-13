s=input("enter a string")
t="the"
c=s.split()
d=0
for i in range(0,len(c)):
    if(c[i]==t):
        d=d+1
print(d)
