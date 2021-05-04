c=[2,4]
s=0
for i in c:
    num=(input())
    c.append(num)
    if (num >= 'A' and num <= 'Z' or num >= 'a' and num <= 'z'):
        break
    t=eval(num)
    s=s+t
print(s)