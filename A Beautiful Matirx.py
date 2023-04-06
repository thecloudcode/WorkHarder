x=[]
a=0
b=0
for i in range(5):
    x.append(list(map(int,input().split())))
    if x[i].count(1)==1:
        a=i
        b=x[i].index(1)
print(abs(2-a)+abs(2-b))