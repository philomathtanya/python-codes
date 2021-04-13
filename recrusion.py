s=input("enter a string")
def ritesh(s):
    if len(s)==0:
        return s
    else:
        return ritesh(s[1:])+s[0]
print(ritesh(s))
