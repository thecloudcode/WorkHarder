import pickle

# students={'Usha':97,'Sakshi':46,'Shreya':49,'Swastika':89}
# f=open('Book1','wb')
# pickle.dump(students,f)
# f.close()
#
# f=open('Book1','rb')
# d=pickle.load(f)
# print(d)
# for i,j in d.items():
#     if j>50:
#         print(i)


# f=open('textfile.txt','r')
# c=0
# while 1:
#     d=f.read(20)
#     if (d):
#         c+=len(d)
#         print('position:',f.tell(),'count:',c)
#     else:
#         break
# print('total: ',c)


# f=open(input("Enter filename: "),'r')
# content = f.read()
# n = int(input('Enter number of characters: '))
# last_n_chars = content[-n:]
# print(last_n_chars)

# try:
#     f1=open('textfile.txt','r')
#     f2=open('textfile2.txt','w')
#     f2.write(f1.read())
#     f2.close()
#     f1.close()
#     f2=open('textfile2.txt','r')
#     print(f2.read())
# except FileNotFoundError:
#     print('Hehe! no file.')

# with open('textfile.txt','w') as f:
#     f.write(input("Enter data: "))
#     f.close()

# name=list(map(str,input().split()))
# f=open('textfile3.txt','wb')
# pickle.dump(name,f)
# f.close()
# f=open('textfile3.txt','rb')
# print(pickle.load(f))

# import csv
# f=open('textfile3.txt','r')
# ro=csv.reader(f,delimiter=',')
# print(ro)
# l=list(ro)
# print(l)
# for i in l:
#     print(i)
# f.close()
#
# f=open('textfile3.txt','w')
# wo=csv.writer(f,delimiter=',')
# wo.writerow([1,2,3,4])
# wo.writerow([11,22,33,44])
# f.close()
#

import csv
f=open("textfile3.txt","a")
wo=csv.writer(f,delimiter=",")
n=int(input("Enter the number of students: "))
lr=[]
for i in range(n):
    rn=int(input("Enter the roll number: "))
    name=input("Enter your name: ")
    a=int(input("Enter the age: "))
    c=input("Enter the class: ")
    p=input("Enter the percentage: ")
    lr.append([rn,name,a,c,p])
wo.writerows(lr)
f.close()
