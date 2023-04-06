xx=input()
s=list(xx)
x=[ord(i) for i in s[1::] if 97<=ord(i)<=122]
if len(x)==0:
    print((s[0].upper() if 97<=ord(s[0])<=122 else s[0].lower() if 65<=ord(s[0])<=90 else s[0])+xx[1::].lower())
else:
    print(xx)

# if (len(x)==1 and x[0]==ord(s[0])) or len(x)==0:


