n=int(input())
s=input()
x=0
xx=1
while(xx<=n):
    # xx+=x*(x+1)/2
    xx+=x
    if (xx-1)<=n-1:
        print(s[xx-1],end="")
    else:
        break
    x+=1
# print(xx)