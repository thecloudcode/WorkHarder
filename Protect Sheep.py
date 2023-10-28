a,b=map(int,input().split())
x=[]
flag=True

for _ in range(a):
    s=input()
    if 'WS' in s or 'SW' in s:
        flag=False
    x.append(s)

if flag:
    for i in range(a):
        for j in range(b):
            if i<a-1:
                if x[i][j]=='W' and x[i+1][j]=='S' or x[i][j]=='S' and x[i+1][j]=='W':
                    flag=False
                    break

if flag:
    print("YES")
    for i in x:
        for j in range(b-1):
            print('D' if i[j]=='.' else i[j],end ="")
        print('D' if i[b-1]=='.' else i[b-1])
else:
    print("NO")