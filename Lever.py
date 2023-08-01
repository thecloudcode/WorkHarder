s=list(input())
x=s.index('^')
left=0
right=0
for i in range(len(s)):
    if i<x and s[i]!='=':
        left+=int(s[i])*(x-i)
    if i>x and s[i]!='=':
        right+=int(s[i])*(i-x)
print("balance" if left==right else "left" if left>right else "right")
