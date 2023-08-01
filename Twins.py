n=int(input())
x=sorted(list(map(int,input().split())))[::-1]
all=0
c=0
xx=sum(x)
for i in x:
    if(xx-all)<all:
        break
    c+=1
    all+=i
print(c)