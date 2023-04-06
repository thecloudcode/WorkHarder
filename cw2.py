l=[[{"Aditya":["Milkcakes","Spade"]},{"Akshat":["Leather"]},{"Raghul":["Temples"]}]]
d={}
keys=[]
values=[]
for i in l[0]:
    # print(i)
    for a,b in zip(list(i.keys()),list(i.values())):
        if len(b)>1:
            d[a+"1"]=b[0]
            d[a+"2"]=b[1]
        else:
            d[a]=b[0]
print(d)
