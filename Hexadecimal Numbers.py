n=int(input())
total=0
def p(a):
    global total
    if a<=n:
        total+=1
        p(a*10)
        p(a*10+1)

p(1)
print(total)
# for i in range(1,len(str(n))):
#     if i==1:
#         total+=1
#     else:
#         combinations = ((i-1)*2)
#         total+=combinations
# for i in range(int('1'+'0'*(len(str(n))-1)),n+1):
#     i=str(i)
#     if '2' in i or '3' in i or '4' in i or '5' in i or '6' in i or '7' in i or '8' in i or '9' in i:
#         continue
#     else:
#         print(i)
#         total+=1
# print(total)