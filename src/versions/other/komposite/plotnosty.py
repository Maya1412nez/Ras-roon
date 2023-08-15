import numpy as np 
from matplotlib import pyplot as plt 
import collections


plt.title("Изменение плотности от количества соды") 
plt.xlabel("количество соды (%)") 
plt.ylabel("плотность") 
# plt.plot(0, 1.05, 'ro') # 1:1
# plt.plot(10.34, 0.918, 'ro-') # 2:3
# plt.plot(14.46, 0.867, 'ro') #1:2
# plt.plot(28.28, 0.608, 'ro') 2:5



x, y = [1, 2, 3, 4, 5], [0.85, 0.75, 0.81, 0.84, 0.73]
x1, y1 = [2, 5], [0.75, 0.73]
x2, y2 = [1, 3, 4], [0.85, 0.81, 0.84]
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([0, 10.34, 14.46], [1.05, 0.918, 0.867])  # Plot some data on the axes.
plt.plot(x2, y2, linestyle='dashed')
plt.plot(x1, y1, linestyle='dashed')
plt.plot(x, y, 'ro')
plt.plot(x1, y1, 'go')
for i in range(len(x)):
    plt.text(x[i]+0.1, y[i], f'{y[i]} ')
# plt.text(x[-1] - 0.2, y[-1] + 0.01, 'ПВХ')
plt.plot(5.5, 0.8, 'wo')
plt.show()