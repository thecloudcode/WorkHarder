
def min_operations_to_balance_string(T, test_cases):
    results = []
    for _ in range(T):
        N, K, S = test_cases [_]
        count_0 = [0]*K
        count_1 = [0]*K
        for i in range(N):
            if S[i]=='0':
                count_0[i % K] += 1
            else:
                count_1[i % K] += 1
        min_operations = float('inf')
        for i in range(K):
            min_operations = min(min_operations, sum(count_0) - count_0[i] + sum(count_1) - count_1[i])
        results.append(min_operations)

    return results

test_cases=[]
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    S=input().strip()
    test_cases.append((N,K,S))

results = min_operations_to_balance_string(,test_cases)
for result in results:
    print(result)