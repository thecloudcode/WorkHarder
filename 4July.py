# import numpy as np
# B = np.array([[10, 20, 30, 40],
#               [50, 60, 70, 80],
#               [90, 100, 110, 120],
#               [130, 140, 150, 160]])
# np.append(B,[1,2,3,4])
# print(B)

import numpy as np

# Create a 2-dimensional NumPy array
my_array = np.array([[1, 2, 3],
                     [4, 5, 6]])

# Append a new row at the end of the array
new_row = np.array([[7, 8, 9]])
modified_array = np.append(my_array, new_row, axis=0)

print("Original array:")
print(my_array)
print("\nModified array after appending:")
print(modified_array)
