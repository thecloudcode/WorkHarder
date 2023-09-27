for _ in range(int(input())):
    l=-((10**9)-1)
    h=10**9+1
    s=input()
    if s[1]==' ':
        if s[0]=='<':
            if s[-1]=='N':
                print("No, <")
                print(int(s[2:-2:]))
                l=max(l,int(s[2:-2:]))
            else:
                print("Yes, >")
                print(int(s[2:-2:])-1)
                h=min(h,int(s[2:-2:])-1)
        if s[0]=='>':
            if s[-1]=='N':
                print("No, >")
                print(int(s[2:-2:]))
                h=min(h, int(s[2:-2:]))
            else:
                print("Yes, >")
                print(int(s[2:-2:])+1)
                l=max(l,int(s[2:-2:])+1)
    elif s[2]==' ':
        if s[0]+s[1]=='<=':
            if s[-1]=='N':
                print("No, <=")
                print(int(s[3:-2:])+1)
                l=max(l,int(s[3:-2:])+1)
            else:
                print("Yes, <=")
                print(int(s[3:-2:]))
                h=min(h,int(s[3:-2:]))
        if s[0]+s[1]=='>=':
            if s[-1]=='N':
                print("No, >=")
                print(int(s[3:-2:])-1)
                h=min(int(s[3:-2:])-1,h)
            else:
                print("Yes, >=")
                print(int(s[3:-2:]))
                l=max(l,int(s[3:-2:]))
    # print(l,h)
    # print(int(s[3:-2:]))
    # print(int(s[2:-2:]))
    if l<=h:
        if h!=((10**9)+1):
            print(h)
        else:
            print(l)
    else:
        print("Impossible")