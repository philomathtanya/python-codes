s=input("")
d=s.split()
k=[]
for i in d:
    if(d.count(i)>1 and(i not in k) or d.count(i)==1):
        k.append(i)
print("".join(k))