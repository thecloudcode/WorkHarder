from collections import defaultdict
s=list(input())
x=list(input())
hash=defaultdict(lambda:0)

for i in s:
    if i==' ':
        continue
    hash[ord(i)-65]+=1

flag=True
# print(dict(hash))


for i in x:
    if i==' ':
        continue
    if hash[ord(i)-65]>0:
        hash[ord(i)-65]-=1
    else:
        flag=False
        break
# print(dict(hash))
print("YES" if flag else "NO")