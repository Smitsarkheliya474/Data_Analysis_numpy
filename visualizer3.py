import matplotlib.pyplot as plt
import numpy as np

x=np.array(['Java','Python','Php','Javascript','C#','C++'])
y=np.array([22.2,17.6,8.8,8,7.7,6.7])

mycolor=['#B7C3F3','pink','lightskyblue','purple','royalblue','#4F6272']
plt.bar(x,y,color=mycolor)
plt.title('Bar Chart')
plt.show()

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(data, bins=6)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
x = [1, 3, 5, 7, 9]
y = [10, 13, 7, 12, 21]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Chart')
plt.show()

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 20]

mycolor = ['lightskyblue','pink','#B7C3F3','purple','royalblue']
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.scatter(x,y,color=mycolor)
plt.show()

sizes = ['Java','Python','Php','Javascript','C#','C++']
labels = [22.2,17.6,8.8,8,7.7,6.7]

mycolor = ['lightskyblue','pink','#B7C3F3','purple','royalblue','#4F6272']
fig=plt.figure(figsize=(8,5))
plt.pie(y,labels=x,autopct='%1.1f%%',colors=mycolor)
plt.title('Pie Chart')
plt.show()

categories = ['A', 'B', 'C']
values1 = [10, 15, 25]
values2 = [5, 10, 15]

plt.bar(categories, values1, label='Value1')
plt.bar(categories, values2, label='Value2', bottom=values1)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.legend()
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 20]

plt.fill_between(x, y, alpha=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Chart')
plt.show()