c=0
for i in range(int(input())):
    x=input()
    if x[0] in '0123456789':
        x=int(x)
        if x<18:
            c+=1
    else:
        if x=="ABSINTH" or x=="BEER" or x=="BRANDY" or x=="CHAMPAGNE" or x=="GIN" or x=="RUM" or x=="SAKE" or x=="TEQUILA" or x=="VODKA" or x=="WHISKEY" or x=="WINE":
            c+=1
print(c)