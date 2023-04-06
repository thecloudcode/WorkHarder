import math
# def prime(num):
#     if num==1:
#         return True
#     if num>2:
#         for i in range(2,num):
#             if num%i==0:
#                 return True
#     return False

def primeFactors(n):
    if (n % 2 == 0):
        d[2] = 0
    while n % 2 == 0:
        d[2] += 1
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if (n % i == 0):
            d[i] = 0
        while n % i == 0:
            # print(i)
            d[i] += 1
            n = n / i
    if n > 2:
        d[n] = 1
    return(len(list(d.keys())))

for _ in range(int(input())):

    global d
    d = {}
    n=int(input())
    i=([n].copy())[0]
    while(i>0):
        if(n%i==0 and primeFactors(i)>1 and primeFactors(n//i)>1):
            if i==1:
                print(n)
            elif n//i==1:
                print(i)
            else:
                print(i+(n//i))
            break
        i-=1




# import math
# def primeFactors(n):
#     if (n % 2 == 0):
#         d[2] = 0
#     while n % 2 == 0:
#         d[2] += 1
#         n = n / 2
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if (n % i == 0):
#             d[i] = 0
#         while n % i == 0:
#             # print(i)
#             d[i] += 1
#             n = n / i
#     if n > 2:
#         d[n] = 1
# for _ in range(int(input())):
#     n=int(input())
#     d={}
#
#     primeFactors(n)
#     print(d)
#     summ=0
#     for i,j in d.items():
#         summ+=i*j
#     print(summ)
