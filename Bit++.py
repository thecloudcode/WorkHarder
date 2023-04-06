x = 0
for _ in range(int(input())):
    s=input()
    x+=1 if (s=="++X" or s=="X++") else -1
print(x)