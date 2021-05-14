n=int(input())
s=set()
for i in range (n):
    t=input()
    c=t.casefold()
    s.add(c)
l=list(s)
t=set()
for i in l:
    for  ch in i:
        if(ch=='a' or ch=='e' or ch=='i' or ch=='o'or ch=='u'):
               t.add(i)
print(t)

