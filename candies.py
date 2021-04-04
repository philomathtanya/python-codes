n=int(input("no.of  kids"))
c=int(input("no.of  candies"))
s=0
for i in range(1,n+1):
    a=int(input(print("no of demand of",i,"student:")))
    s=s+a
if s==c:
    print("yes,demand are meet")
else:
    print("no,demands are not meet")
