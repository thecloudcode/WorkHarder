a,b,c=map(int,input().split())
money=0
for i in range(1,c+1):
    money+=i*a
print(money-b if (money-b)>0 else 0)
