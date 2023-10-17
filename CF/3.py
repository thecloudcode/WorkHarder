# import numpy as np
for _ in range(int(input())):
    n=int(input())
    one=[]

    for __ in range(n):
        s=input()
        x=[]
        for i in s:
            x.append(ord(i))
        one.append(x)
            # two[j][__]=ord(i)

    c=0
    for i in range(n//2):
        for j in range(n//2):
            maxx=max(one[i][j], max(one[n-j-1][i], max(one[n-i-1][n-j-1], one[j][n-i-1])))
            c+=maxx-one[i][j]
            c+=maxx-one[n-j-1][i]
            c+=maxx-one[n-i-1][n-j-1]
            c+=maxx-one[j][n-i-1]



    # print(one)
    print(int(c))
