x=[ {"Dg set": "Diesel generator"}, {"Organization": "Organisation"}, {"Group": "Organization"}, {"Orange": "Kinnu"}, {"Orange": "narangi"} ]
a=[]
b=[]
for i in x:
    f = True
    for j in a:
        if list(i.keys())[0] in j:
            j.append(list(i.values())[0])
            f=False
        elif list(i.values())[0] in j:
            j.append(list(i.keys())[0])
            f=False
    if f:
        a.append([list(i.keys())[0],list(i.values())[0]])
print(a)
