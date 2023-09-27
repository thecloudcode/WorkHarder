for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    flag=True
    if n%2==0 and x[(n//2)-1]==x[(n//2)]==(n//2)-1:
        flag=False
    if flag:
        for i in range(n):
            if x[i]<min(i,n-i-1):
                flag=False
                break
    print("Yes" if flag else "No")