from collections import defaultdict
x=defaultdict(lambda:0)
y=defaultdict(lambda:0)

# c=0
n=int(input())
a, b = map(int, input().split())
x[a]+=1
y[b]+=1
c=0
for _ in range(n-1):
    a, b = map(int, input().split())

    if x[a]==0 and y[b]==0:
        c+=1
    x[a]+=1
    y[b]+=1

print(c)