n=int(input())
s=input()

start=0
end=0
for i in range(n-1):
    if s[i]==s[i+1]:
        start+=1
    else:
        break
for i in range(n - 1):
    if s[n-i-2]==s[n-i-1]:
        end+=1
    else:
        break
# print(start,end)
modd=998244353
if s[0]==s[-1]:
    print((start+2)%modd*(end+2)%modd)
else:
    print((start+end+3)%modd)