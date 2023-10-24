from collections import defaultdict
x=defaultdict(lambda : 0)
x['Q'],x['R'],x['B'],x['n'],x['P']=9,5,3,3,1
x['q'],x['r'],x['b'],x['N'],x['p']=9,5,3,3,1
w=0
b=0

for _ in range(8):
    s=input()
    for i in s:
        if i.islower():
            b+=x[i]
        else:
            w+=x[i]
print("White" if w>b else "Black" if b>w else "Draw")