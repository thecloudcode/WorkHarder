# f=open('textfile.txt','w')
# print("Enter 5 words: ")
# for i in range(5):
#     f.write(input()+"\n")
# f.close()
# f=open('textfile.txt','r')
# print(f.readlines())
# f.close()

# import datetime
# f=open('textfile.txt','w')
# f.write(str(datetime.datetime.now()))
# f.close()
# f=open('textfile.txt','r')
# print(f.readlines())
# f.close()

# try:
#     f=open('data.txt','r')
#     for i in f.readlines():
#         print(i)
# except FileNotFoundError:
#     print('No such file')

# f=open('message.txt','w')
# f.write('Python is awesome!')
# f.close()
# f=open('data.txt','r')
# print(f.read())
# f.close()

# try:
#     n=input("Enter filename: ")
#     x=input("Enter text: ")
#     f=open('n'+'.txt','w')
#     f.write(x)
# except FileNotFoundError:
#     print('Nof found!')

# f=open('textfile.txt','r')
# print(f.tell())
# print(f.read(5))
# print(f.tell())
# print(f.readline())
# print(f.tell())

# try:
#     f=open('textfile.txt','r')
#     l=0
#     c=0
#     for i in f:
#         l+=1
#         c+=len(i)
#     print(l)
#     print(c)
# except FileNotFoundError:
#     print('Not found!')


# try:
#     file = open('textfile.txt', 'r+')
#     # file.read(3)
#     # file.seek(3)
#     filesize=file.seek(0,2)
#     print(filesize)
#     n=int(input("Enter the number of bytes: "))
#     file.seek(filesize-n,0)
#     data=file.read()
#     print(data)
# except:
#     print('error')

import pickle
# f=open('Book1','wb')
# l=[input() for i in range(5)]
# pickle.dump(l,f)
# f.close()

# f=open('Book1','rb')
# l=pickle.load(f)
# d={}
# for j in l:
#     d[j]=int(input("Enter marks: "))
# print(l)
# print(d)
# f.close()
#
# f=open('Book1','wb')
# pickle.dump(d,f)
# f.close()

f=open('Book1','rb')
a=pickle.load(f)
print(a)
for i,j in a.items():
    if j>=51:
        print(i)
f.close()


