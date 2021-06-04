s1=input()
s2=input()
a=len(s1)
s1=s1[2:a-2]
b=len(s2)
s2=s2[2:b-2]
l1=s1.split("', '")
print(l1)

l2=s2.split("', '")
c=0
for i in l1:
    for j in l2:
        if(sorted(i)==sorted(j)):
            c=c+1
print(c)
