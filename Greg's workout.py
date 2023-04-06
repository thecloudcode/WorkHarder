n=int(input())
chest=0
biceps=0
back=0
x=list(map(int,input().split()))
for i in range(n):
    if i%3==0:
        chest+=x[i]
    elif i%3==1:
        biceps+=x[i]
    elif i%3==2:
        back+=x[i]
xx=max(chest,max(biceps, back))
a print("chest" if xx==chest else "biceps" if xx==biceps else "back")