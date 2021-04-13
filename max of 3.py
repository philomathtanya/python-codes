n1=eval(input("enter a first no"))
n2=eval(input("enter a second no"))
n3=eval(input("enter a third no"))
if n1 > n2 and n1 > n3:
    print("greater no is",n1)
elif n2 > n3 and n2 > n1:
    print("greater no is", n2)
else:
    print("greater no is", n3)
