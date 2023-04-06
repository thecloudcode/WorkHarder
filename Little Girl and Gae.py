from collections import defaultdict
x=list(input().lower())

hash=defaultdict(lambda:0)
odd=0

for i in range(len(x)):
    hash[ord(x[i])-97]+=1

for i in range(len(x)):
    if hash[ord(x[i])-97]%2==1:
        odd+=1

# print(hash,odd)
if odd==0 or odd==1:
    print("First")
else:
    if odd%2==0:
        print("Second")
    else:
        print("First")