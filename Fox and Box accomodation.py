from collections import defaultdict
d=defaultdict(lambda:0 )

n=int(input())
x=sorted(list(map(int,input().split())))
xx=[[] for i in range(100)]
ind=0

for i in x:
    flag=False
    for j in range(ind+1):
        if d[j]<=i:
            if d[j]==0:
                ind+=1
            d[j]+=1
            flag=True
            break
    # if flag==False:
    #     ind+=1
    #     d[ind]+=1
# print(dict(d))
print(ind)



