i=int(input())
j=int(input())

m=[]
n=[]
for a in range(i):
    ls=[]
    for b in range(j):
       ls.append(int(input()))
    m.append(ls)
#print(m)
print("the first matrix is:")
for a in range(i):
    for b in range(j):
        print(m[a][b],end=" ")
    print("")
for a in range(i):
    ls1=[]
    for b in range(j):
       ls1.append(int(input()))
    n.append(ls1)
#print(n)
print("the second matrix is:")
for a in range(i):
    for b in range(j):
        print(n[a][b],end=" ")
    print("")
res=[]

for a in range(len(m)):
    re=[]
    for b in range(len(n[0])):
        #re=[]
        s=0
        for c in range(len(n)):
            s+=m[a][c]*n[c][b]
        #print(s)
        re.append(s)
    res.append(re)
print("the resultant matrix is:")
for a in range(i):
    for b in range(j):
        print(res[a][b],end=" ")
    print("")
