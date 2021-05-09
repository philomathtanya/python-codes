dict={'name':"tanya bansal",'class':"btech cs",'section':"A",'university':"G.l.A,",'place':"G.l.A,"}
r={}
for key,value in dict.items():
    if value not in r.values():
        r[key]=value
print(r)


