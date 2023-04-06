for _ in range(int(input())):
    n=int(input())
    s=list(input())
    x=""
    xx=int(s[0])
    for i in range(1,n):
        if xx+int(s[i])>1:
            xx-=int(s[i])
            x+="-"
        else:
            xx+=int(s[i])
            x+="+"
    print(x)
