# Create a line plot using Matplotlib to visualize a simple dataset

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y,'bo-')
plt.title("Line Plot Example")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

# Generate a scatter plot using Seaborn with random data points

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(42)
num_points = 100
random_data = {
    'X':np.random.rand(num_points),
    'Y':np.random.rand(num_points)
}
df = pd.DataFrame(random_data)
sns.set_style("whitegrid")
sns.scatterplot(x='X',y='Y',data=df)
plt.title("Scatter Plot with Random Data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Customize the color and style of a Seaborn bar plot

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Category': ['A','B','C','D'],
    'Value': [4,7,1,8]
}
df = pd.DataFrame(data)
custom_palette = ["blue","green","red","yellow"]
sns.set_palette(custom_palette)
sns.set_style("whitegrid")
sns.barplot(x="Category",y="Value",data=df)
plt.title("Customized Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Create a figure with multiple subplots using Matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.linespace(0,2*np.pi,100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2*x)
y4 = np.cos(2*x)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,8))
axes[0,0].plot(x,y1)
axes[0,0].set_title('Sin(x)')
axes[0,1].plot(x,y2)
axes[0,1].set_title('Cos(x)')
axes[1,0].plot(x,y3)
axes[1,0].set_title('Sin(2x)')
axes[1,1].plot(x,y4)
axes[1,1].set_title('Cos(2x)')
plt.tight_layout()
plt.show()

# Use Seaborn to create a grid of histograms for different columns in a DataFrame.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = {
    'Column 1': [1,2,2,3,3,3,4,4,4,4],
    'Column 2': [10,15,20,25,30,35,40,45,50,55],
    'Column 3': [5,5,10,10,15,15,20,20,25,25]
}
df = pd.DataFrame(data)
sns.set(style = "whitegrid")
grid = sns.histplot(data=df,bins=10,kde=True)
plt.show()

# Generate a box plot using Seaborn to show the distribution of a numerical variable.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'NumericalVariable': [15,20,25,30,35,40,45,50,55,60,65]
}
df = pd.DataFrame(data)
sns.set(style = "whitegrid")
sns.boxplot(x=df['NumericalVariable'])
plt.show()

# Create a violin plot to compare the distribution of two different variables.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Variable1' : [25,30,35,40,45,50,55,60,65,70],
    'Variable2' : [20,25,30,35,40,45,50,55,60,65]
}
df = pd.DataFrame(data)
sns.set(style="whitegrid")
sns.violinplot(data=df,palette="muted",inner="quartile")
plt.show()

# •	Use Matplotlib to create a bar plot for categorical data.

import matplotlib.pyplot as plt
categories = ['Category A','Category B','Category C','Category D']
values = [15,30,25,40]
plt.bar(categories, values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot for Categorical Data')
plt.show()

# Employ Seaborn to make a count plot for categorical variables in a DataFrame.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {'Category' : ['A','B','A','C','B','A','C','A','B','C']}
df = pd.DataFrame(data)
sns.set(style = "whitegrid")
sns.countplot(x='Category',data=df,palette='pastel')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Count Plot')
plt.show()

# Create a heatmap using Seaborn for a correlation matrix

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Feature1':[1,2,3,4,5],
    'Feature2':[5,4,3,2,1],
    'Feature3':[1,2,1,2,1],
    'Feature4':[3,3,3,3,3]
}
df = pd.DataFrame(data)
correlation_matrix = df.corr()
sns.set(style="white")
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',linewidths=.5)
plt.title('Correlation Matrix Heatmap')
plt.show()

#•	Create a custom colormap for a Matplotlib heatmap.

