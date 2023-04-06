x=list(map(int,input().split()))
x.sort()
print(abs(x[0]-x[1])+abs(x[1]-x[2]))
