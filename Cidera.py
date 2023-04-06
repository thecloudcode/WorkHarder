import math
a=int(input())
b=int(input())

d=0
while(b>1):
    b/=a
    d+=1
if b==1:
    print("YES")
    print(d-1)
else:
    print("NO")