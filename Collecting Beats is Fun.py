from collections import defaultdict

k=int(input())
d=defaultdict(lambda: 0)
d['.']=0
for i in range(4):
    x=list(input())
    for j in x:
        if j=='.':
            continue
        d[j]+=1

xx=max(list(d.values()))
# print(xx)
print("YES" if xx<=2*k else "NO")