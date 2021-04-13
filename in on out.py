r=eval(input("enter a radius"))
c1=int(input("enter centre of circle c1"))
c2=int(input("enter centre of circle c2"))
a1=int(input("enter arbitrary  point of circle a1"))
a2=int(input("enter arbitrary  point of circle a2"))
d=( (a2-c2)**2 + (a1-c1)**2 )**0.5
if d == r:
    print("point is on the circle")
elif d>r:
    print("point is outside the circle")
else:
    print("point is inside the circle")
