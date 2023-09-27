s=input()
n=len(s)
i=0
ab=False
ba=False
aba=False
last=-1
while(i<n-1):
    # print(s[i:i+3])
    if i+3<n and (s[i:i+3:]=='ABA' or s[i:i+3]=='BAB') and aba==False:
        aba=True
        i+=3
        continue
    if s[i]=='A' and ab==False:
        if s[i+1]=='B':
            ab=True
            i+=2
            continue
    if s[i]=='B' and ba==False:
        if s[i+1]=='A':
            ba=True
            i+=2
            continue
    i+=1
print("YES" if (ab and ba) or (aba and ba) or (aba and ab) else "NO")
