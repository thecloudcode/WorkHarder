from collections import defaultdict
d=defaultdict(lambda:0)
n=int(input())
x=list(map(int,input().split()))

maxx=0
s=[4,8,15,16,23,42]
c=0
minn=n
def check():
    for i in range(5):
        if d[s[i]]<d[s[i+1]]:
            return False
    return True

for i in x:
    d[i]+=1
    if check()==False:
        c+=1
        d[i]-=1

# minn=0
for i in s:
    if minn>d[i]:
        minn=d[i]
print(n-6*minn)