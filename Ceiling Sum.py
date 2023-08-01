import math

def cal(a,b,x):
    return int(math.ceil((b - x) / 2) + math.ceil((x - a) / 2))

for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==b:
        print(0)
    else:
        a1=math.ceil((a+b)/2)
        a2=math.floor((a+b)/2)
        xx=[math.ceil((b - a1) / 2) + math.ceil((a1 - a) / 2),
                    math.ceil((b - a2) / 2) + math.ceil((a2 - a) / 2), math.ceil(b / 2) - math.ceil(a / 2),
                                  math.ceil((b - b) / 2) + math.ceil((b - a) / 2),
                                  math.ceil((b - a) / 2) + math.ceil((a - a) / 2)]
        if a+1 in range(min(a,b),max(a,b)+1):
            xx.append(cal(a,b,a+1))
        if a-1 in range(min(a,b),max(a,b)+1):
            xx.append(cal(a,b,a-1))
        if b+1 in range(min(a,b),max(a,b)+1):
            xx.append(cal(a,b,b+1))
        if b-1 in range(min(a,b),max(a,b)+1):
            xx.append(cal(a,b,b-1))

        print(int(max(xx)))

