import math
from collections import defaultdict

d = defaultdict(lambda: 0)

# Open input and output files
with open("input.txt.txt", "r") as input_file, open("output2.txt", "w") as output_file:
    t = int(input_file.readline().strip())  # Read the number of test cases

    for case in range(1, t + 1):
        n = int(input_file.readline().strip())  # Read n for the current case
        x = sorted(list(map(int, input_file.readline().strip().split())))  # Read and sort the integers

        if n == 5:
            z = max((x[2] + x[4]) / 2 - (x[0] + x[1]) / 2, (x[3] + x[4]) / 2 - (x[0] + x[2]) / 2)
            if math.floor(z) == z:
                z = int(z)
            output_file.write(f"Case #{case}: {z}\n")
        else:
            z = (x[-1] + x[-2]) / 2 - (x[0] + x[1]) / 2
            if math.floor(z) == z:
                z = int(z)
            output_file.write(f"Case #{case}: {z}\n")
