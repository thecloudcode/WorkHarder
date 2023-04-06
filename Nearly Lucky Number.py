n=list(input())
c=0
for i in n:
    if i=='7' or i=='4':
        c+=1
# print(c)
# print(list(str(c)))
# print()
print("YES" if list(str(c)).count('4')+list(str(c)).count('7')==len(str(c)) else "NO")
