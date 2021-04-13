t=int(input("input a year"))
if ((t%4==0) or(t%100==0 and t%400==0)):
    print("leap year")
else:
    print("not a leap year")
