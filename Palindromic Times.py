a,b=map(str,input().split(':'))
# print(a,b)
# print(int(str(a)[::-1]))
x=["00","01","02","03","04","05","10","11","12","13","14","15","20","21","22","23"]
if int(a)==23 and int(b)>=32:
    print("00:00")
else:
    if int(b)>=60 or int(a[::-1])>=60 or int(b)>=int(a[::-1]):
        for i in x:
            if int(i)>int(a):
                print(i+":"+i[::-1])
                break
    else:
        print(a+":"+a[::-1])


