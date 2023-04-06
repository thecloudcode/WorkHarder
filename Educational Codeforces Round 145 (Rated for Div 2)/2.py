import math
import decimal
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    # a,b = map(int, input().split())
    N = int(input())
    # print(int(math.sqrt(int(N-1))))
    D = decimal.Decimal
    n = D(N-1)

    with decimal.localcontext() as ctx:
        ctx.prec = 300
        x = n.sqrt()
        print(int(x))

    # s = input()
    # x = list(map(int, input().split()))
    # anse=-1
    # anso=-1
    # if n==1:
    #     print(0)
    # else:
    #     ne=[n].copy()[0]
    #     no=[n].copy()[0]
    #     # print(ne,no)
    #     i=0
    #     while(True):
    #         if i%2==0 and ne>=0:
    #             if i==0:
    #                 ne-=1
    #             else:
    #                 if i*4>ne:
    #                     anse=max(anse,i)
    #                     ne=0
    #                     # print(1,"anse", anse, "ne", ne)
    #                 else:
    #                     anse=max(anse,i)
    #                     ne-=4*i
    #                     # print(2,"anse", anse, "ne", ne)
    #
    #         elif no>=0:
    #             if i*4>no:
    #                 anso=max(anso,i)
    #                 no=0
    #                 # print(1, "anso", anso, "no", no)
    #             else:
    #                 anso=max(anso,i)
    #                 no-=4*i
    #                 # print(1, "anso", anso, "no", no)
    #         if no==0 and ne==0:
    #             break
    #         i+=1
    #     print(min(anso,anse))