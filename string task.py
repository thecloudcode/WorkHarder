s=list(input().lower())
x=[i for i in s if i not in ['a','e','y','i','o','u']]
print('.'+'.'.join(x) if len(x)>0 else "")
