import itertools

def can_be_sorted(parts):
    # generate all possible permutations of each part
    permutations = [sorted(list(itertools.permutations(part))) for part in parts]

    # generate all possible combinations of the permutations
    combinations = list(itertools.product(*permutations))

    # check if any combination is in non-decreasing lexicographical order
    for combo in combinations:
        if combo == tuple(sorted(combo)):
            return True

    return False

# read input
T = int(input())
for case in range(1, T+1):
    P = int(input())
    parts=list(map(str,input().split()))

    if can_be_sorted(parts):
        print("Case #{}: {}".format(case, "POSSIBLE"))
    else:
        print("Case #{}: {}".format(case, "IMPOSSIBLE"))
