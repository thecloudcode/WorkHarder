def beauty_value(arr):
    """
    Given an array 'arr', returns the sum of beauty values for all subarrays of 'arr' containing at least two numbers.
    """
    n = len(arr)
    result = 0
    for i in range(n):
        m1 = arr[i]
        for j in range(i+1, n):
            m2 = arr[j]
            if m2 < m1:
                m1, m2 = m2, m1
            result += m1 ^ m2
    return result

# Main function
if __name__ == '__main__':
    t = int(input()) # number of test cases
    for _ in range(t):
        n = int(input()) # size of the array
        arr = list(map(int, input().split())) # elements of the array
        result = beauty_value(arr)
        print(result)
