import math
for _ in range(int(input())):
    nn=int(input())
    n=[nn].copy()[0]
    ans=[nn]
    while(1):
        x=n/2
        up=math.ceil(x)
        down=n//2
        # last=ans[-1]
        if down==0 and up==0:
            break
        elif up==0:
            if nn//ans[-1]!=nn//down:
                ans.append(down)
        elif down==0:
            if nn//ans[-1]!=nn//up:
                ans.append(up)

        elif up!=0 and down!=0:

            if nn//up==nn//down:
                # ans.append(up)
                if nn // ans[-1] != nn // down:
                    ans.append(down)
            else:
                if nn // ans[-1] != nn // up:
                    ans.append(up)
                if nn // ans[-1] != nn // down:
                    ans.append(down)

        n//=2
    ans.append(0)
    print(len(ans))
    for i in ans[::-1]:
        print(i, end=" ")
    print()