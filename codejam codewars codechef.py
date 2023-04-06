for _ in range(int(input())):
    n=int(input())
    s=list(input())
    i=0
    f=True
    while i < len(s) and s[i] in ['m', 'M']:
        i += 1
    if i == 0:
        f= False
    while i < len(s) and s[i] in ['e', 'E'] and f:
        i += 1
    if i == 1:
        f=False
    while i < len(s) and s[i] in ['o', 'O'] and f:
        i += 1
    if i == 2:
        f=False
    while i < len(s) and s[i] in ['w', 'W']:
        i += 1
    if(i == len(s) and f): f=True
    else: f=False
    print("YES" if f else "NO")
