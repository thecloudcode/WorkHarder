s=input()
i=0
if s[0]!=" " and s[0]!='"':
    s=' '+s
if s[-1]!=" " and s[-1]!='"':
    s=s+' '
n=len(s)
l=len(s)

while(i<l):
    if s[i]=='"':
        i+=1
        x=""
        while(i<l):
            if s[i]=='"':
                print("<"+x+">")
                i+=1
                x=""
                # print(i)
                break
            else:
                x+=s[i]
                i+=1
    if i>=n:
        break
    if s[i]==" " and i+1<n and s[i+1]=='"':
        i+=1
        continue
    elif s[i]==" " and i!=n-1 and s[i+1]!=' ':
        i+=1
        x=""
        # print("gotta")
        while(i<l):
            if s[i]==" ":
                print("<" + x + ">")
                # i += 1
                x = ""
                break
            else:
                # print(x)
                x+=s[i]
                i+=1
    else:
        i+=1
# "RUn.exe O" "" "   2ne, " two! . " "