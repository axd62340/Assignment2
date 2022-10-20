import matplotlib.pyplot as plt
import numpy as np

y = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
mylabels = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
myexplode = [0.2, 0, 0, 0,0,0]
plt.pie(y,labels=mylabels, explode = myexplode,autopct='%1.1f%%')
plt.show()


