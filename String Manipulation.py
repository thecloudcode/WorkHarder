for _ in range(int(input())):
    n=int(input())

    s=input()
    i=2
    ansi=1
    ans=s
    while(i<n):
        if (n-i)%2==0:
            z=s[i::]+s[:i:]
        else:
            z = s[i::] + s[:i:][::-1]
        if z<ans:
            ans=z
            ansi=i+1
        i+=1
    print(ans)
    print(ansi)