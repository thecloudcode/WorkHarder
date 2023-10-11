from collections import defaultdict
d=defaultdict(lambda:0)
n,m=map(int,input().split())
row=-1
col=-1
flag=True
for i in range(n):
    s=input()
    for j in range(m):
        if s[j]=='*':
            d[j]+=1
            d[i]+=1
            if d[j]>1:
                row=j
                if col==-1:
                    col=i
            if d[i]>1:
                col=i
                if row==-1:
                    row=j
            if row!=-1:
                if row!=j:
                    flag=False
                else:
                    continue
            if col!=-1:
                if col!=i:
                    flag=False
print("YES" if flag else "NO")
if flag:
    print(col,row)