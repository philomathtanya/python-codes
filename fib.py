n=int(input("enter upto the no"))
n1=0
n2 = 1
print("0,1", sep='/n')
while (n-2>0):
 t = n1 + n2
 print(t)
 n1 = n2
 n2 = t
 n = n - 1
