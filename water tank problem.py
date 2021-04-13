h=10
r=5
f=10
t=int(input("enter a time"))
vt=3.14*r*r*h
vwtr=f*t
if vwtr>vt:
	print("overflow")
	print("volume of ",vwtr-vt)
elif vwtr==vt:
	print("tank full")
else:
	print("underflow condition")
