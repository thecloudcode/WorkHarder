# cook your dish here
def co(x):
    i = 0
    z = 0
    y = 0
    while (i < len(x) - 1):
        if x[i] + x[i + 1] == '01':
            z += 1
        elif x[i] + x[i + 1] == '10':
            y += 1
        i += 1
    if z == y:
        return 1
    else:
        return 0


for tc in range(int(input())):
    s = list(input())
    # x=s.count('10')
    # y=s.count('01')
    # if x==0 and y==0:
    #     if len(s)%2==0:
    #         print(len(s)//2)
    #     else:
    #         print((len(s)//2)+1)
    # else:
    #     print(abs(x-y))
    c = 0
    for i in range(len(s)):
        ns = s.copy()
        if (s[i] == "0"):
            ns[i] = "1"
        elif (s[i] == "1"):
            ns[i] = "0"
        # ns="".join(ns)
        c += co(ns)
    print(c)