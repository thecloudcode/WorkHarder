for _ in range(int(input())):
    str = input().strip()
    c = []
    n = len(str)
    s = []
    for i in range(n):
        if str[i] == 'B':
            if c:
                x = c.pop()
                str = str[:x] + '*' + str[x+1:]

        elif str[i] == 'b':
            if s:
                x = s.pop()
                str = str[:x] + '*' + str[x+1:]

        elif 'A' <= str[i] <= 'Z':
            c.append(i)

        elif 'a' <= str[i] <= 'z':
            s.append(i)

    print(''.join([ch for ch in str if ch != '*' and ch != 'B' and ch != 'b']))



