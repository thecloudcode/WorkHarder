n=input()
print(max(int(n),max(int(n[:-1:]),int(n[:-2:]+n[-1]))))


