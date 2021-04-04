sa=eval(input("enter the shipping amount"))
if sa > 25000:
    d=(20 / 100)*sa
    print("GOLD , amount is ",d)
elif sa >=10000 and sa<=25000:
    f=(10 / 100)*sa
    print("SILVER , amount is ",f)
else:
    print("BRONZE, amount is ",(5/100)*sa)