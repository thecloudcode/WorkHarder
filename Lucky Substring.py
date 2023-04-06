s=input()
if '4' in s or '7' in s:
    print('4' if s.count('4')>=s.count('7') else '7')
else:
    print(-1)