n=int(input())
s=set()
for i in range (n):
    c=int(input())
    s.add(c)
b=int(input("input no"))
if b in s:
        c=s.remove(b)
        print("removed no is",b)
print(s)
