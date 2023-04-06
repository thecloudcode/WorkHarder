n=int(input())
x=""
for i in range(n):
    if (i+1)%4==1:
        x+='a'
    elif (i+1)%4==2:
        x+='b'
    elif (i+1)%4==3:
        x+='c'
    elif (i+1)%4==0:
        x+='d'
print(x)