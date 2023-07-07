import numpy as np 
from matplotlib import pyplot as plt 
import collections


plt.title("Зависимость массы эпоксидной смолы от времени") 
plt.xlabel("Время (сутки)") 
plt.ylabel("Масса образца") 



# x, y = [0, 10.34, 14.46, 28.28], [1.05, 0.918, 0.867, 0.608]
# # fig, ax = plt.subplots()  # Create a figure containing a single axes.
# # ax.plot([0, 10.34, 14.46], [1.05, 0.918, 0.867])  # Plot some data on the axes.
# for i in range(0, len(x)):
#     plt.plot(x[i:i+2], y[i:i+2], 'ro-')
# plt.show()
def get_data(name):
    if name == 'Ацетон':
        return([0, 1, 2], [0.661, 0.708, 0.728], 0, 0.03)
    if name == 'KOH':
        return ([0, 1, 2], [0.733, 0.753, 0.762], 0, 0.03)
    if name == 'H2SO4 конц.':
        return([0, 1], [0.887, 1.551], 0.1, 0)
    if name == 'Морская вода':
        return([0, 1, 2], [0.593, 0.603, 0.613], 0, 0.022)

list_of_ress = ['Ацетон', 'KOH', 'H2SO4 конц.', 'Морская вода']
for name in list_of_ress:
    x1, y1, move_x, move_y = get_data(name)
    plt.plot(x1,y1) 
    plt.text(x1[0] + move_x, y1[0] + move_y, name)
    plt.plot(x1,y1, 'bo') 
plt.show()

