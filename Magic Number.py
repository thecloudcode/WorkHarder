s=input()
x=s.count('144')
y=s.count('14')-x
z=s.count('1')-x-y
# print(x,y,z)
if 3*x+2*y+z==len(s):
    print("YES")
else:
    print("NO")