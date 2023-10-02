for _ in range(int(input())):
    n=int(input())
    x=0
    s="abcdefghijklmnopqrstuvwxyz"
    if n==1:
        print('b')
    else:
        x=1
        for i in range(2,n+1):
            if n%i!=0:
                x=i
                break
        print(s[:i:]*(n//i)+s[:n%i:])
