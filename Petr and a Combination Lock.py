n=int(input())
ans=0
s=0
x=[]
for i in range(n):
    x.append(int(input()))
x.sort()
print(x)
for a in x:
    s+=a
    if ans-a>=0:
        ans-=a
    else:
        ans+=a
print("YES" if ans==0 or s%360==0 else "NO")