def find_subarrays(arr):
    n = len(arr)
    subarrays = []

    for i in range(n-2):
        for j in range(i, n):
            subarrays.append(arr[i:j + 1])
    return subarrays

def xor_of_smallest_and_second_smallest(arr):
    smallest = float('inf')
    second_smallest = float('inf')
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return smallest ^ second_smallest


for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    xx=find_subarrays(x)
    ans=0
    for arr in xx:
        smallest = arr[0]
        second_smallest = float('inf')
        for num in arr:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest:
                second_smallest = num
        ans+=smallest ^ second_smallest
    print(ans)

