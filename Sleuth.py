x=list(input().lower())
for i in range(2,len(x)+1):
    if ord(x[-i])>=97 and ord(x[-i])<=122:
        if x[-i] in 'aeiouy':
            print("YES")
            break
        else:
            print("NO")
            break
    else:
        continue
