from collections import defaultdict

for _ in range(int(input())):
    d = defaultdict(lambda: 0)
    xx=[]
    vika=['v','i','k','a']
    n,k=map(int,input().split())
    for i in range(n):
        x=input()
        xx.append(x)
    for i in range(k):
        for j in xx:
            if len(vika)==0:
                break
            if j[i]==vika[0]:
                d[vika[0]]=i
                vika.remove(vika[0])
                break
    # print(dict(d))
    print("YES" if len(vika)==0 else "NO")
