dict=[{"name":True,"class":"10"},{"name":True,"class":"1"},{"name":False,"class":"0"}]
c=0
for i in dict:
    a=i.values()
    for k in a:
        if k ==True:
            c=c+1
print(c)