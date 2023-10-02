import math

def zero(n):
    n=str(n)
    z=0
    for i in n[::-1]:
        if i=='0':
            z+=1
        else:
            break
    return z

for _ in range(int(input())):
    a,b=map(int,input().split())

    bb=str(b)
    z=0

    five=int(b//5)*5
    ten=int(b//10)*10
    # print(five, ten)
    aaa=max(a*b,1)
    bbb=max(a*five,1)
    ccc=max(a*ten,1)

    az=zero(aaa)
    bz=zero(bbb)
    cz=zero(ccc)
    # print(az,bz,cz)
    if max(az,max(bz,cz))==az:
        print(aaa)
    else:
        if bz>cz and bz>az:
            print(bbb)
        elif cz>az:
            print(ccc)
        else:
            print(aaa)
