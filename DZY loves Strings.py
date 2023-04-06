s=input()
n=int(input())
x=list(map(int,input().split()))
ans=0
for i in range(len(s)):
    ans+=(i+1)*(x[ord(s[i])-97])
xx=len(s)+1
for i in range(n):
    ans+=xx*max(x)
    xx+=1
print(ans)