n,k = map(int,input().split())

x = list(map(int,input().split()))
left = 0
s = 0
c = 0
flag = False
for i in x:
    c += 1
    if i + left > 8:
        left = left + i - 8
        s+=8
    else:
        s+=i+left
        left=0
    if s>=k:
        flag=True
        break
print(c if flag else -1)