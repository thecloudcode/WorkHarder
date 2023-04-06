n=list(input())
x=[]
for i in n:
    x.append(int(i))
# print(x)
c=0
xx=0
while(len(x)>1):
    xx=sum(x)
    x=[]
    for i in str(xx):
        x.append(int(i))
    # print(x)
    # x=list(str(xx))
    c+=1
print(c)