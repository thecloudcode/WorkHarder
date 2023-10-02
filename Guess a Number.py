for _ in range(int(input())):
    s=input()
    l=-10**9-1
    gotl=False
    h=10**9+1
    goth=False

    # s=input()
    if s[0]+s[1]=='>=':
        if s[-1]=='Y':
            l=max(int(s[3:-2:]),l)
            # print(l)
            gotl=True
        if s[-1]=='N':
            h=min(int(s[3:-2:],h)-1,h)
            goth=True
    elif s[0]+s[1]=='<=':
        if s[-1]=='Y':
            h=min(int(s[3:-2:]),h)
            goth=True
        if s[-1]=='N':
            l=max(int(s[3:-2:])+1,l)
            gotl=True
    elif s[0]=='>':
        if s[-1]=='Y':
            l=max(int(s[2:-2:])+1,l)
            print(l)
            gotl=True
        if s[-1]=='N':
            h=min(int(s[2:-2:]),h)
            goth=True
    elif s[0]=='<':
        if s[-1]=='Y':
            h=min(h,int(s[2:-2:])-1)
            # print(h)
            goth=True
        else:
            l=max(l,int(s[2:-2:]))
            gotl=True
print(l,h)
if l>h:
    print("IMPOSSIBLE")
elif gotl:
    print(l)
elif goth:
    print(h)
else:
    print("IMPOSSIBLE")