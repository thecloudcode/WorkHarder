summ = 0
c = 0
banned=[1,6,5]
n=5
maxSum=6
x=int((-1 + (1 + 8 * maxSum) ** 0.5) / 2)
# print(x)
summ=int(x*(x+1)/2)
# print(summ)
b=[i for i in banned if 1<=i<=x]
# print(b)
summ-=sum(b)
# print(summ)
z=x-len(b)
# print(z)
for i in range(x+1,n+1):
    if(summ+i>maxSum ):
        break
    elif i not in banned:
        z+=1
print(z)

