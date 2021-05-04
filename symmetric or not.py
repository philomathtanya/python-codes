i=int(input())
j=int(input())

m=[]
for a in range(i):
    ls=[]
    for b in range(j):
       ls.append(int(input()))
    m.append(ls)
for a in range(i):
    for b in range(j):
        print(m[a][b],end=" ")
    print("")
z=1
for a in range(i):
    for b in range(j):
        if m[b][a]!=m[a][b]:
            z=2
if(z==1):
  print("symmetric")
else:
  print("not symmetric")

