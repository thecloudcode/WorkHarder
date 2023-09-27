flag=True
north=0
south=0
for _ in range(int(input())):
    t,s=map(str,input().split())

    if south-north==20000:
        if s!="North":
            flag=False
    if north-south==0 or (north==0 and south==0):
        if s!="South":
            flag=False
    if int(t)>20000 and (s=="North" or s=="South"):
        flag=False
    if s=="North":
        north+=int(t)
        # if north-south)>20000:
        #     flag=False
    if s=="South":
        south+=int(t)
        if south-north>20000:
            flag=False
    if south-north<0:
        flag=False

print("YES" if south-north==0 and flag else "NO")
