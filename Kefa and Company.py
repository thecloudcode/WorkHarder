
n,k=map(int,input().split())
x=[]
xx=[]

def bubble_sort():
    n = len(x)

    for i in range(n):
        # Flag to optimize the algorithm by stopping if no swaps are made in a pass
        swapped = False

        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            if x[j] > x[j + 1]:
                # Swap the elements
                x[j], x[j + 1] = x[j + 1], x[j]
                xx[j], xx[j + 1] = xx[j + 1], xx[j]
                swapped = True

        # If no two elements were swapped in inner loop, the array is already sorted
        if not swapped:
            break


for i in range(n):
    a,b=map(int,input().split())
    # d[a]=b
    x.append(a)
    xx.append(b)

bubble_sort()
i=0
j=0
ans=0
c=0
while(1):
    if abs(x[i]-x[j])<k:
        # print('yes')
        c+=xx[j]
        j+=1
        ans=max(ans,c)
    else:
        # print('no')
        if i==j:
            j+=1
            i+=1

        else:
            c-=xx[i]
            i+=1
    if j==n:
        break
print(ans)