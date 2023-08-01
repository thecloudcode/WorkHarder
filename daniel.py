import collections


def find(text:str)->int:
    counter=collections.Counter(text)
    for i,c in enumerate(text):
        if counter[c]==1:
            return i
    return -1

print(find(input()))