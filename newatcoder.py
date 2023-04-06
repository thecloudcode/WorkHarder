# Python3 program for above approach

# Function to find minimum flips
# required to remove all 0s from
# a given binary string
def minOperation(s):
    # Length of given string
    n = len(s)

    # Stores the indices of
    # previous 0s
    temp1 = -1
    temp2 = -1

    # Stores the minimum operations
    ans = 0

    # Traverse string to find minimum
    # operations to obtain required string
    for i in range(n):

        # Current character
        curr = s[i]

        # If current character is '0'
        if (curr == '1'):

            # Update temp1 with current
            # index, if both temp
            # variables are empty
            if (temp1 == -1 and temp2 == -1):
                temp1 = i

            # Update temp2 with current
            # index, if temp1 contains
            # prev index but temp2 is empty
            elif (temp1 != -1 and temp2 == -1 and
                  i - temp1 == 1):
                temp2 = i

            # If temp1 is not empty
            elif (temp1 != -1):

                # Reset temp1 to -1
                temp1 = -1

                # Increase ans
                ans += 1

            # If temp2 is not empty but
            # temp1 is empty
            elif (temp1 == -1 and temp2 != -1 and
                  i - temp2 != 1):

                # Reset temp2 to -1
                temp2 = -1

                # Increase ans
                ans += 1

    # If both temp variables are not empty
    if (temp1 != -1 and temp2 != -1):
        ans += 2

    # Otherwise
    elif (temp1 != -1 or temp2 != -1):
        ans += 1

    # Return the answer
    return ans


# Driver Code
if __name__ == '__main__':
    for _ in range(int(input())):
        n=int(input())

        print(minOperation(input()))

# This code is contributed by mohit kumar 29
