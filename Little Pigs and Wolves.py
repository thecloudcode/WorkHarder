from collections import defaultdict
n,m=map(int,input().split())

x=[list('.'*(m+2))]
for i in range(n):
    lol=list('.'+input()+'.')
    x.append(lol)
x.append(list('.'*(m+2)))

# pigs=defaultdict(lambda:0)
# wolf=defaultdict(lambda:[])
c=0

for i in range(1,n+1):
    for j in range(1,m+1):
        # if x[i][j]=='P':
        #     if x[i][j+1]=='W':
        #         pigs[i,j]+=1
        #     if x[i+1][j]=='W':
        #         pigs[i,j]+=1
        #     if x[i-1][j]=='W':
        #         pigs[i,j]+=1
        #     if x[i][j-1]=='W':
        #         pigs[i,j]+=1
        if x[i][j]=='W':
            if x[i][j+1]=='P':
                # wolf[i,j].append([i,j+1])
                x[i][j+1]='.'
                c+=1
            elif x[i+1][j]=='P':
                c += 1
                x[i+1][j]='.'
                # wolf[i,j].append([i+1,j])
            elif x[i-1][j]=='P':
                c += 1
                x[i-1][j]='.'
                # wolf[i,j].append([i-1,j])
            elif x[i][j-1]=='P':
                c += 1
                x[i][j-1]='.'
                # wolf[i,j].append(i,j-1)

print(c)



