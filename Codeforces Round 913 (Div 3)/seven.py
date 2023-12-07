def min_operations_to_sort(arr):
    n = len(arr)

    # Function to check if the array is sorted
    def is_sorted(a):
        return all(a[i] <= a[i + 1] for i in range(len(a) - 1))

    # Function to perform the shift operation
    def shift(a):
        return [a[-1]] + a[:-1]

    # Function to perform the reverse operation
    def reverse(a):
        return a[::-1]

    # Try all possible combinations of operations
    for operations in range(3 ** n):
        operations_left = operations
        current_arr = arr.copy()
        count = 0

        # Apply operations based on the ternary representation of operations
        for i in range(n):
            if operations_left % 3 == 1:
                current_arr = shift(current_arr)
                count += 1
            elif operations_left % 3 == 2:
                current_arr = reverse(current_arr)
                count += 1

            operations_left //= 3

        # Check if the current combination of operations sorts the array
        if is_sorted(current_arr):
            return count

    # If no combination of operations sorts the array, return -1
    return -1

# Example usage
for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))

    print(min_operations_to_sort(x))
