def maximum(n,m,c):


    max_distance = 0

    for i in range(n):
        if i+1 not in c: # check if the house is not celebrating
            left = i
            while left >= 0 and left+1 not in c:
                left -= 1 # move left until a celebrating house is found
            right = i
            while right < n and right+1 not in c:
                right += 1 # move right until a celebrating house is found
            distance = min(i-left, right-i) # find the minimum distance to a celebrating house
            max_distance = max(max_distance, distance)

    return max_distance

print(maximum(7,4,[1,2,3,4]))

def main():
    n,m=[int(val) for val in input().split()]
    x=input().split()
    c=[]
    for i in range(m):
        c.append(int(x[i]))
    print(maxNum(n,m,c))

main()