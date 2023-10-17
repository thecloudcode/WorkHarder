from collections import defaultdict
for _ in range(int(input())):
    d=defaultdict(lambda :0)
    a,b,c=map(int,input().split())

    if a==b==c:
        print("YES")
    else:
        x=[a,b,c]
        maxx=max(x)
        minn=min(x)

        x.append(maxx-minn)
        x.append(minn)
        x.remove(maxx)

        if len(set(x))==1:
            print("YES")
        else:
            maxx = max(x)
            minn = min(x)

            x.append(maxx - minn)
            x.append(minn)
            x.remove(maxx)
            if len(set(x)) == 1:
                print("YES")
            else:
                maxx = max(x)
                minn = min(x)

                x.append(maxx - minn)
                x.append(minn)
                x.remove(maxx)
                if len(set(x)) == 1:
                    print("YES")
                else:
                    print("NO")



