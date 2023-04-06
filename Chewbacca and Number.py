s=list(input())
ss=""
for i in s:
    if i=='9' and ss == "":
        ss += i
    elif int(i)>4:
        ss+=str(9-int(i))
    else:
        ss+=i
print(ss)