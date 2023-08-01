from collections import defaultdict

db=defaultdict(lambda:0)

for _ in range(int(input())):
    s=input()
    if db[s]==0:
        db[s]+=1
        print("OK")
    else:
        print(s+str(db[s]))
        db[s]+=1

