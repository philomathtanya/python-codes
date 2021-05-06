a=int(input())
d={}
for i in range(1,a+1):
    x={i:i*i}
    d.update(x)
print(d)