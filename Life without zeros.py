a=input()
b=input()
c=int(a)+int(b)
x=[i for i in list(str(c)) if i!='0']
x=int(''.join(x))

aa=[i for i in list(a) if i!='0']
bb=[i for i in list(b) if i!='0']
cc=int(''.join(aa))+int(''.join(bb))
xx=int(''.join(list(str(cc))))

print("YES" if x==xx else "NO")

