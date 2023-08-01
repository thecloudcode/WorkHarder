import numpy as np

# print(np.arange(1,13).reshape(3,4))

# A=np.array([[1,2,1],[0,1,0],[2,3,4]])
# B=np.array([[2,5,1],[6,7,1],[1,8,1]])
# print(A+B,'\n\n',A-B,'\n\n',A*B)

# A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# trans=A.T
# print(trans,np.sum(trans))

# print(np.array([1,2,3,4,5,6,7,8,9,10,11,12])[9:12])
# print(np.flip(np.array([1,2,3,4,5,6,7,8,9,10,11,12])))

# marks=np.array([81,97,98,62,76,88])
# print(np.sum(marks),np.max(marks),np.argmax(marks),np.min(marks),np.argmin(marks),np.mean(marks),np.std(marks))

# marks=np.array([[10,20,30],[40,50,60],[70,80,90],[30,40,50]])
# print(np.sum(marks))
# for i in range(len(marks)):
#     print('Row',i+1,":",sum(marks[i]))
# for i in range(len(marks[0])):
#     print('Col',i+1,":",sum(marks[:,i]))

# A = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.vstack((A,np.array([7,8,9]))))

# A = np.array([[1, 2,3],[3,4,5]])
# print(np.hstack((A,np.array([[9],[10]]))))

# from scipy import linalg
# a=np.array([[3,6],[5,10]])
# b=np.array([30,100])
# res=linalg.solve(a,b)
# print(res)

import pandas as pd
import numpy as np

# Original DataFrame
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack', 'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
df = pd.DataFrame(d)

# Add 'Experience' column with random values between 1 and 10
df['Experience'] = np.random.randint(1, 11, size=len(df))

# Print the updated DataFrame
print(df)

