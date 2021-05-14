x=int(input())
n=int(input())
s=set()
for i in range (n):
    t=int(input())
    s.add(t)
s1=set()
for i in s:
    if i % x==0:
       s1.add(i)
print(s1)
n=int(input())
s=set()
for i in range (n):
    t=int(input())
    s.add(t)
s2=set()
for i in s:
    if i % x==0:
       s2.add(i)
print(s2)
print("the multiple of x present in both set but not in both",s1^s2)

