s=input("")
n=int(input())
t=int(r / n)
for i in range(0,len(s),t):
    f=s[i:i+t]
    print(f)

