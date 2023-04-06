x=list(input())
y=list(input())

indx=[]
indy=[]
if len(x)!=len(y):
    print("NO")
elif len(x)>=2:
    for i in range(len(x)):
        if x[i]!=y[i]:
            indx.append(x[i])
            indy.append(y[i])

    if len(indx)==0:
        print("YES")
    elif len(indx)==2:
        if indx[0]==indy[1] and indx[1]==indy[0]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    if x[0]==y[0]:
        print("YES")
    else:
        print("NO")