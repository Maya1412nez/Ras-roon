import numpy as np 
from matplotlib import pyplot as plt 
import collections


plt.title("Изменение плотности от количества микросфер") 
plt.xlabel("количество микросфер (гр)") 
plt.ylabel("плотность композита") 
# plt.plot(0, 1.05, 'ro') # 1:1
# plt.plot(10.34, 0.918, 'ro-') # 2:3
# plt.plot(14.46, 0.867, 'ro') #1:2
# plt.plot(28.28, 0.608, 'ro') 2:5



x, y = [0, 10.34, 14.46], [1.05, 0.918, 0.867]
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([0, 10.34, 14.46], [1.05, 0.918, 0.867])  # Plot some data on the axes.
plt.plot(x, y)
plt.plot(x, y, 'ro')
# plt.text(x[-1] - 0.2, y[-1] + 0.01, 'ПВХ')
plt.show()

