c=0
s=input()
s=list(s)
for i in range(len(s)-2):
    for j in range(i+1,len(s)):
        if (s[i:j:].count('L')==s[i:j:].count('R')):
            print(s[i:j:])
            c+=1
print(c)