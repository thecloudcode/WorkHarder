x=list(input())
ans=0
for i in x:
    if i=='>':
        ans+=8
    if i=='<':
        ans+=9
    if i=='+':
        ans+=10
    if i=='-':
        ans+=11
    if i=='.':
        ans+=12
    if i==',':
        ans+=13
    if i=='[':
        ans+=14
    if i==']':
        ans+=15

print(ans%1000003)