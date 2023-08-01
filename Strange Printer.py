s=input()
# starting_index={}
ending_index={}
l=len(s)
for i in range(l):
    ending_index[s[i]]=i
    # starting_index[s[l-i-1]]=l-i-1
final={}
c=0
for i in range(l):
    if i not in final or final[i]!=s[i]:
        for j in range(i,ending_index[s[i]]+1):
            final[j]=s[i]
        c+=1
    # print(final)
print(c)


