for _ in range(int(input())):
    n=int(input())
    s=input().lower()
    x=len(list(set(list(s))))
    if 'm' in s and 'e' in s and 'o' in s and 'w' in s and x==4:
        m=s.index('m')
        mm=s.rindex('m')
        e=s.index('e')
        ee=s.rindex('e')
        o=s.index('o')
        oo=s.rindex('o')
        w=s.index('w')
        ww=s.rindex('w')
        if(m<=mm<e<=ee<o<=oo<w<=ww):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")