from collections import defaultdict
d=defaultdict(lambda : -1)
s=list(input())
n=int(input())
x=list(map(int,input().split()))

for n in x:
    d[n] = 1 if d[n]!=1 else 0
cond = False
# print(d)
l=len(s)
for i in range(len(s)//2):
    if d[i+1] == 1:
        cond = True if cond==False else False

    if cond:
        t=s[i]
        s[i]=s[l-i-1]
        s[l-i-1] = t
for i in s:
    print(i,end="")