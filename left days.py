d=int(input("enter the date"))
m=int(input("enter the month"))
ld=30-d
ml=12-m
tdl=365 - ( ld+(ml*30) )
print("total days left are =",tdl)