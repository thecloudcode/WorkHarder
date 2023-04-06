# cook your dish here
def dist(a,b,c,d):
    return((((a-c)**2)+((b-d)**2))**0.5)
for _  in range(int(input())):
    N,x1,y1,x2,y2=map(int,input().split())
    x=min[dist(x1,x1,y1,1),dist(x1,1,y1,y1),dist(x1,N,y1,y1),dist(x1,x1,y1,N)]
    y=min[dist(x2,x2,y2,1),dist(x2,1,y2,y2),dist(x2,N,y2,y2),dist(x2,x2,y2,N)]
    print(min(dist(x1,y1,x2,y2),(x+y+2)))