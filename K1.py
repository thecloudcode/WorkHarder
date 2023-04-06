s=input("str: ")
n=int(input("num: "))
k=0
if(n<len(s) and n>=0):
    print("output:",end=" ")
    for i in s:
        if(s[k]==s[n]):
            k+=1
            continue
        k+=1
        print(i,end="")
    print()
else:
    print("num should be positive, less than the length of str")