s=input()
c=0
for i in range(len(s)-1):
    if s[i]+s[i+1]=='ab':
        c+=1
        back=i-1
        front=i+2
        while(back>=0):
            if s[back]=='a':
                c+=2
            back-=1
        while(front<len(s)):
            if s[front]=='b':
                c+=1
            front+=1
print(c)
