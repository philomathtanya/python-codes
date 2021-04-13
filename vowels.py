n = input("enter a string")
t = str.lower(n)
v=0
c=0
sp=0
d=0
for i in range(0,len(n)):
    if n[i] in ('a','e','i','o','u'):
        v=v+1
    elif(n[i]>='a' and n[i]<='z'):
        c=c+1
    elif(n[i]>='0' and n[i]<='9'):
        d=d+1
    else:
        sp=sp+1
print("vowels=",v)
print("consonants=",c)
print("digits=",d)
print("spaces=",sp)

