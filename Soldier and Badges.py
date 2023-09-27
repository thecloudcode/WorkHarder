from collections import defaultdict
d=defaultdict(lambda :0)

n=int(input())
x=sorted(list(map(int,input().split())))
for i in x:
    d[i]+=1
ans=0
start=1
# print(x)
for i in x:
    if d[i]>1:
        while(d[start]!=0 or start<=i):
            start+=1
        d[i]-=1
        ans+=i-start
        d[start]+=1
        # print(start,i)
print(abs(ans))

#
#
# n=int(input())
# x=sorted(list(map(int,input().split())))
#
# ans=0
# print(x)
# for i in range(n):
#     if x[i]!=i+1:
#         ans+=x[i]-i+1
# print(ans)
#
