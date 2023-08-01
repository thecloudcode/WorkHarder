dp={}
def soupserve(a,b):
    if (a,b) in dp:
        return dp[(a,b)]
    if a<=0 and b>0:
        return 1
    elif a<=0 and b<=0:
        return 0.5
    elif b<=0 and a>0:
        return 0
    result= 0.25*(soupserve(a-100,b-0)+soupserve(a-75,b-25)+soupserve(a-50,b-50)+soupserve(a-25,b-75))
    dp[(a,b)]=result
    return result
print(soupserve(100,100))
# print(dp)