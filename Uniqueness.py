from collections import defaultdict
d=defaultdict(lambda:0)
dd=defaultdict(lambda:0)

n=int(input())
x=list(map(int,input().split()))

start=0
end=0
for i in range(n):
    d[x[i]]+=1
    if d[x[i]]>1:
        start=i
        break
for i in range(n):
    dd[x[n-i-1]]+=1
    if dd[x[n-i-1]]>1:
        end=n-i-1
        break

# print(end,start)
print(abs(end-start)+1 if end!=0 and start!=0 else 0)