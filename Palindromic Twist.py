for _ in range(int(input())):
    n=int(input())
    s=list(input().lower())
    x=[]
    f=True
    for i in range((n//2)):
        if s[i]=='a' or s[i]=='z':
            if s[i]==s[n-i-1]:
                continue
            elif s[i]=='a' and s[n-i-1]!='c':
                f=False
                break
            elif s[i]=='z' and s[n-i-1]!='x':
                f = False
                break
        if s[i]!=s[n-i-1] and str(ord(s[i])+1)!=str(ord(s[n-i-1])+1) and str(ord(s[i])+1)!=str(ord(s[n-i-1])-1) and str(ord(s[i])-1)!=str(ord(s[n-i-1])+1) and str(ord(s[i])-1)!=str(ord(s[n-i-1])-1):
            f=False
            break
        #     x.append(i)
        # else:
        #     if i=='z':
        #         x.append('y')
        #     elif i=='a':
        #         x.append('b')
        #     else:
        #         if str(ord(i)+1) in x:
        #             x.append(chr(ord(i)+1))
        #         else:
        #             x.append(chr(ord(i)-1))
    # print(x)
    print("YES" if f else "NO")