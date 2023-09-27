for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    if x[0]!=n:
        print("NO")
        continue
    left=[]
    for i in x:
        left.append(x[0]-i)
    find=1
    c=0
    right=[]
    i=0
    while(i<n):
        if x[n-i-1]>=find:
            right.append(i)
            find+=1
            if find-1>=x[n-i-1]:
                i+=1
            if len(right)==n or find>x[0]:
                break
        elif find>=x[n-i-1]:
            i+=1
            if len(right)==n or find>x[0]:
                break


    print("YES" if left==right else "NO")