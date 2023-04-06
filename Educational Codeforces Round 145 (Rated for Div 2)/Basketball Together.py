import math
n,w=map(int,input().split())
x=sorted(list(map(int,input().split())))

x=x[::-1]
c=0
teams=0
for i in x:
    z=w//i
    z+=1
    # print(i,":",z)
    if z>n-c:
        break
    if i*z>w:
        c+=z
        teams+=1
    else:
        break
print(teams)


