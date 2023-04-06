import math
from collections import defaultdict

def find(s):
    count = 1
    result = []
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            if count >= 1:
                result.append((s[i], count))
            count = 1
        else:
            count += 1
    if count >= 1:
        result.append((s[len(s)-1], count))
    return result

# x=find_consecutive_chars("aabbbbcd")
# print(x)
for _ in range(int(input())):
#     # d = defaultdict(lambda:0)
#     # a,b = map(int, input().split())
    n = int(input())
    s = input()
    x=find(s)
    ans=""
    for i in x:
        i=list(i)
        if i[1]%2==1:
            ans+=i[0]
        else:
            ans+=i[0]*2
    print(ans)

#     x=['A']
#     v=[0]
#     c=1
#     ch=''
#     for i in range(n):
#         # x.append(s[i])
#         if s[i]==x[-1]:
#             c+=1
#             ch=s[i]
#         else:
#             x.append(ch)
#             v.append(c)
#             c=1
#     print(x,v)
    # x=['A']
    # i=0
    # while(i<n):
    #     if s[i]==s[i+1]==s[i+2]:
    #         x.append(s[i])
    #         i+=2
    #     elif x[-1]==s[i]:
    #         i+=1
    #         continue
    #     elif s[i]==s[i+1]:
    #         x.append(s[i])
    #         x.append(s[i])
    #         i+=1
    #     i+=1
    # print(''.join(x[:-1:]))
    # x = list(map(int, input().split()))