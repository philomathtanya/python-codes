n=int(input("enter a roll no"))
c=0
for i in range(1,501):
    if i % n ==0:
        c=c+1
print("no of students whose phone is in off mode",c)


