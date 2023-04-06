
global d
d=[]
def maxSumPathUtil(i, j, matrix, dp, n,d):
    if n==-1:
        return 0
    if i==-1:
        i=C-1
    if i==C:
        i=0
    if j==R:
        j=0
    if j==-1:
        j=R-1
    if [i,j] in d:
        return -100010
    if dp[i][j] != -100007:
        return dp[i][j]

    up = matrix[i][j] + maxSumPathUtil(i, j+1, matrix, dp,n-1,d)
    left = matrix[i][j] + maxSumPathUtil(i-1, j, matrix, dp,n-1,d)
    right = matrix[i][j] + maxSumPathUtil(i+1, j, matrix, dp,n-1,d)
    down = matrix[i][j] + maxSumPathUtil(i, j-1, matrix, dp,n-1,d)
    dp[i][j] = max(up, left, down, right)
    if dp[i][j]==left:
        if len(d)>=4:
            d.pop(-4)
            # d.pop(-3)
            d.pop(-1)
            d.pop(-1)
        d.append([i-1,j])
    elif dp[i][j]==right:
        if len(d)>=4:
            d.pop(-4)
            d.pop(-3)
            # d.pop(-2)
            d.pop(-1)
        d.append([i+1,j])
    elif dp[i][j]==up:
        if len(d)>=4:
            # d.pop(-4)
            d.pop(-1)
            d.pop(-1)
            d.pop(-1)
        d.append([i,j+1])
    elif dp[i][j]==down:
        if len(d)>=4:
            d.pop(-4)
            d.pop(-3)
            d.pop(-2)
            # d.pop(-1)
        d.append([i,j-1])
    return dp[i][j]

C,R,S=map(int,input().split())
x=list(map(int,input().split()))
mat=[]
for i in range(1,R+1):
    z=list(map(int,input().split()))
    mat.append(z)
dp=[]
for i in range(6):
    dp.append([-100007,-100007,-100007,-100007,-100007,-100007])
print(maxSumPathUtil(0,0,mat,dp,x[0],d))
print(d)
print(len(d))