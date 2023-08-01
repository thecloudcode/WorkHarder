n=5
m=4
arr=[ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]
ans=[]
c=0
s1 = 0
e1 = n - 1
s2 = 0
e2 = n - 1
s3 = m - 1
e3 = n - 1
s4 = 0
e4 = m - 1
while(c<=m*n):

    for i in range(s1,e1):
        ans.append(arr[s1][i])
        c+=1
        if(c>m*n):
            break
    s1+=1
    e1-=1
    # ------------

    for i in range(s2,m-1):
        ans.append(arr[i][e2])
        c+=1
        if (c > m * n):
            break
    s2+=1
    e2-=1
    #--------------

    for i in range(e3):
        ans.append(arr[s3][e3-i])
        c += 1
        if (c > m * n):
            break
    s3-=1
    e3-=1
    #--------------

    for i in range(e4):
        ans.append(arr[s4][e4-i])
        c += 1
        if (c > m * n):
            break
    s4+=1
    e4-=1
print(ans)