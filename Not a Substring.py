for _ in range(int(input())):
    s=input()

    if s=='()':
        print("NO")
    elif '))' in s or '((' in s:
        print("YES")
        print('()'*len(s))
    else:
        print("YES")
        print('('*len(s)+')'*len(s))