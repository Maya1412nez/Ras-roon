import numpy as np 
from matplotlib import pyplot as plt 
import collections



plt.title("Изменение массы образцов из эпоксидной смолы во времени") 
plt.xlabel("Время, сутки") 
plt.ylabel("Масса образца, гр") 



# x, y = [0, 10.34, 14.46, 28.28], [1.05, 0.918, 0.867, 0.608]
# # fig, ax = plt.subplots()  # Create a figure containing a single axes.
# # ax.plot([0, 10.34, 14.46], [1.05, 0.918, 0.867])  # Plot some data on the axes.
# for i in range(0, len(x)):
#     plt.plot(x[i:i+2], y[i:i+2], 'ro-')
# plt.show()
def get_data(name):
    days = [1, 2, 3, 4]
    if name == 'Ацетон':
        notes = [(4 - 0.4, 0.718 + 0.07, 'Отломился кусок')]
        return(days, [0.661, 0.708, 0.728, 0.718], 0, 0.03, notes)
    if name == 'KOH':
        notes = []
        return (days, [0.733, 0.753, 0.762, 0.769], 0, 0.03, notes)
    if name == 'H2SO4 конц.':
        notes = [(1 + 0.05, 1.551, 'Растворился')]
        return([0, 1], [0.887, 1.551], 0.1, 0, notes)
    if name == 'Морская вода':
        notes = []
        return(days, [0.593, 0.603, 0.613, 0.629], 0, 0.022, notes)

list_of_ress = ['Ацетон', 'KOH', 'H2SO4 конц.', 'Морская вода']
for name in list_of_ress:
    x1, y1, move_x, move_y, notes = get_data(name)
    for el in notes:
        plt.text(el[0], el[1], el[2])
        print(el[2])
    plt.plot(x1,y1) 
    plt.text(x1[0] + move_x, y1[0] + move_y, name)
    plt.plot(x1,y1, 'bo') 
plt.show()

