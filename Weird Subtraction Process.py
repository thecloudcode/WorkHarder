x,y=map(int,input().split())
# x=max(a,b)
# y=min(a,b)
# flag=False
while(x!=0 and y!=0):
    if x>=2*y:
        x=x-(x//(2*y))*2*y
    if y>=2*x and x!=0:
        y=y-(y//(2*x))*2*x
    if x<2*y and y<2*x:
        break
print(x,y)