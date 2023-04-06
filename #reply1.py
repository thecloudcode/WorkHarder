C,R,S=map(int,input().split())
x=list(map(int,input().split()))

mat=[]
teleport={}
maxx=[]
maxx=maxx[::-1]

for i in range(1,R+1):
    z=list(map(str,input().split()))
    for i in z:
        maxx.append(i)
    mat.append(z)

maxx.sort()
maxx=maxx[::-1]

for i in range(r):
    teleport[i, j]=[]
    for j in range(c):
        if mat[i][j]=='*':
            if(j>=0):
                teleport[i,j].append(mat[i][j-1])
            if(i>=0):
                teleport[i,j].append(mat[i-1][j])
            if(i<=R-1):
                teleport[i,j].append(mat[i+1][j])
            if(j<=C-1):
                teleport[i,j].append(mat[i][j-1])

xx=[]
xxx=[]
for k in x:
    for i in range(r):
        for j in range(c):
            if mat[i][j]==maxx[0]:
                xx.append(mat[i][j])
                a=([i].copy)[0]
                b=([j].copy)[0]
                for l in range(k-1):
                    up=mat[a][b+1]
                    down=mat[a][b-1]
                    left=mat[a-1][b]
                    right=mat[a+1][b]
                    goal=max(up,down,right,left)
                    if goal==up:
                        




