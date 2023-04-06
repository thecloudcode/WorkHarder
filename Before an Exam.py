for _ in range(1):
    d,t = map(int,input().split())
    arr = [];res = [];total = 0
    for _ in range(d): min,max = map(int,input().split())
    total += min;res.append(min);arr.append(max - min)
    flag = (t == total)
    if(total < t):
        for i in range(d):
            if(arr[i] >= t - total):
                res[i] += t - total
                flag = True
                break
            else:
                res[i] += arr[i]
                total += arr[i]
    print("YES"," ".join(str(i) for i in res),sep = "\n") if flag else print("NO")
