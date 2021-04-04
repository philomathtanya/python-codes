p=eval(input("enter p"))
r=eval(input("enter r"))
t=int(input("enter t"))
ta=p*((1+r/100)**t)
print('%.2f'%ta)
ci=ta-p
print('%.2f'%ci)