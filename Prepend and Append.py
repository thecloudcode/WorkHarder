for _ in range(int(input())):
    n=int(input())
    s=list(input())
    c=0
    for i in range(n//2):
        if s[i]==s[n-i-1]:
            break
        else:
            c+=2
    print(n-c)

