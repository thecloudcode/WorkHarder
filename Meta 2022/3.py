from collections import defaultdict
for _ in range(int(input())):
    d = defaultdict(lambda: 0)

    s=list(input())
    maxc=0
    maxv=0
    tc=0
    tv=0
    for i in s:
        d[i]+=1
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            maxv=max(maxv,d[i])
            tv+=1
        else:
            maxc=max(maxc,d[i])
            tc+=1
    # consonant: tv+2*(tc-maxc)
    # tc+2*(tv-maxv)
    print(f"Case #{_+1}: {min(tc + 2 * (tv - maxv), tv + 2 * (tc - maxc))}")