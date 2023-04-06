a,b=map(int,input().split(":"))
c,d=map(int,input().split(":"))
# print(d,b)
# min=d-b
# if (c-a)%2==0:
#     a+=(c-a)//2
# else:
#     a+=(c-a)//2
#     min+=60
# min=b+(min//2)
# minu=0
# if c>a:
#     minu+=60-b
#     minu+=(c-a-1)*60
#     minu+=d
# else:
#     minu+=d-b
# minu=minu//2
# a+=minu//60
# b+=minu%60

min1=a*60+b
min2=c*60+d
mid=(min1+min2)//2
hrs=mid//60
mins=mid%60
if len(str(hrs))==1:
    hrs="0"+str(hrs)
else:
    hrs=str(hrs)
if len(str(mins))==1:
    mins="0"+str(mins)
else:
    mins=str(mins)
print(hrs+":"+mins)

