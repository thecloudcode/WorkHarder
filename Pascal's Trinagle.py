print("PASCAL'S TRIANGLE")
n=int(input("Enter number of lines required: "))
z=[0,1,0]
print(" "*(n+1),1)
i=0
zz=[0]
for _ in range(n-1):
    for i in range(len(z)-1):
        zz.append(z[i]+z[i+1])
    zzz=[]
    for i in zz[1::]:
        zzz.append(str(i))
    print(" "*(n-_),' '.join(zzz))
    zz.append(0)
    # print(zz)
    z=zz.copy()
    zz=[0]
