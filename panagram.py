s=input("")
k=[]
for i in s:
   if (i>='a'and i<='z'):
    if i not in k :
      k.append(i)
if len(k)==26:
    print("p")
else:
    print("not")
