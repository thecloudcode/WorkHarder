for _ in range(int(input())):
    n=int(input())
    s=input()
    if 'RL' in s:
        print("0")
    else:
        if "LR" in s:
            print(s.index("LR")+1)
        else:
            print("-1")