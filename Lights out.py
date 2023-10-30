x=[]
x.append(list(map(int,input().split())))
x.append(list(map(int,input().split())))
x.append(list(map(int,input().split())))

xx=[[1,1,1],[1,1,1],[1,1,1]]
print(x)
for i in range(3):
    for j in range(3):
        xx[i][j]+=x[i][j]
        if i+1<3:
            xx[i+1][j]+=x[i][j]
        if i-1>=0:
            xx[i-1][j]+=x[i][j]
        if j+1<3:
            xx[i][j+1]+=x[i][j]
        if j-1>=0:
            xx[i][j-1]+=x[i][j]
print(xx)
for i in range(3):
    for j in range(2):
        print("0" if xx[i][j]%2==1 else "1", end="")
    print("0" if xx[i][j] % 2==1 else "1")
