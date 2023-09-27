n=input()
ans=""
carry=False
for i in n[::-1]:
    if carry:
        if int(i)<4:
            ans="4"+ans
            carry=False
        elif int(i)<7:
            ans="7"+ans
            carry=False
        else:
            carry=True
    else:
        if int(i) <= 4:
            ans = "4" + ans
        elif int(i) <= 7:
            ans = "7" + ans
        else:
            carry = True
if carry:
    if ans[0]=="4":
        ans=("7"+ans[1::])
    elif ans[0]=="7":
        ans=("44"+ans[1::])
else:
    ans=(ans)

seven=0
four=0
for i in ans:
    if i=="7":
        seven+=1
    else:
        four+=1

finalans=""
if four==seven:
    print(ans)
elif four<seven:
    for i in ans[::-1]:
        if i=="7":