for _ in range(int(input())):
    n=int(input())
    if(n%2==0):
        print("NO")
    else:
        print("YES")
        m=int((n-1)/2)
        for i in range(1,m):
            print(i,3*m+2+i)
        print(m,4*m+2)
        for i in range(m,m+2):
            print(i+1,2*(m+1)+i-m)

