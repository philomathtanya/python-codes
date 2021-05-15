n=int(input())
s=set()
for i in range (n):
    c=input()
    s.add(c)
r=[]
for i in s:
    p=set(i)
    if len(p) == len(i):
        r.append(i)
print(set(r))


