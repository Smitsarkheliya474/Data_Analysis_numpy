import matplotlib.pyplot as plt
import numpy as np

print("1. horizontal bar chart")
print("2. vertical bar chart")
print("3. pie chart")

s = int(input("Enter Your Choice For Graph  :~"))

if (s == 1):
    x=np.array(['Java','Python','Php','Javascript','C#','C++'])
    y=np.array([22.2,17.6,8.8,8,7.7,6.7])
    mycolor=['#B7C3F3','pink','lightskyblue','purple','royalblue','#4F6272']
    plt.barh(x,y,color=mycolor)
    plt.show()

elif (s == 2):
    x=np.array(['Java','Python','Php','Javascript','C#','C++'])
    y=np.array([22.2,17.6,8.8,8,7.7,6.7])
    mycolor=['#B7C3F3','pink','lightskyblue','purple','royalblue','#4F6272']
    plt.bar(x,y,color=mycolor)
    plt.show()

elif (s == 3):
    x=['Java','Python','Php','Javascript','C#','C++']

    y=[22.2,17.6,8.8,8,7.7,6.7]
    myexplode = [0.2,0,0,0,0,0]
    mycolor = ['#B7C3F3','pink','lightskyblue','purple','royalblue','#4F6272']
    fig=plt.figure(figsize=(10,7))
    plt.pie(y,labels=x,autopct='%1.1f%%',colors=mycolor)
    plt.show()

else :
    print("Wrong choice.........!!")