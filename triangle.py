s1=int(input("enter first side"))
s2=int(input("enter second side"))
s3=int(input("enter third side"))
if(s1+s2>s3 and s2+s3>s1 and s1+s3>s2):
    if(s1==s2==s3):
        print("equilateral triangle")
    elif(s1==s2 or s2==s3 or s1==s3):
        print("isoceles triangle")
    else:
        print("scalene triangle")
else:
    print("invalid triangle")
