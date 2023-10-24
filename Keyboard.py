x=["qwertyuiop","asdfghjkl;","zxcvbnm,./"]

from collections import defaultdict
L=defaultdict(lambda : 0)
R=defaultdict(lambda : 0)

for ii in x:
    for i in range(len(ii)-1):
        L[ii[i]]=ii[i+1]
    for i in range(1,len(ii)):
        R[ii[i]]=ii[i-1]

s=input()
if s=="R":
    xx=input()
    xxx=""
    for i in xx:
        xxx+=R[i]
else:
    xx=input()
    xxx=""
    for i in xx:
        xxx+=L[i]
print(xxx)