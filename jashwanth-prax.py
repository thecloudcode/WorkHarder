s=input()
v="aeiou"
c="bcdfghjklmnpqrstvwxyz"
vowels=0
consonants=0
for i in s:
    if i in v:
        vowels+=1
    elif i in c:
        consonants+=1
print("vowels : ",vowels)
print("consonants : ",consonants)