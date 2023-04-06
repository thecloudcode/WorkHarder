n=int(input())
print("HARD" if list(map(int,input().split())).count(1)>0 else "EASY")