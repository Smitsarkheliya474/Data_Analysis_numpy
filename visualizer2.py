import matplotlib.pyplot as plt
import numpy as np

x=['Python', 'R', 'SQL', 'JAVA', 'NODE JS']
y=[1500000,1360000,1298000,1079000,1370000]

mycolor = ['lightskyblue','pink','#B7C3F3','purple','royalblue']

fig=plt.figure(figsize=(10,7))
plt.pie(y,labels=x,autopct='%1.1f%%',colors=mycolor)
plt.show()
