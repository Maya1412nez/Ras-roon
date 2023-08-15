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

# def build_points():
#     coord1 = (2, )

def get_data(name):
    days = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15]
    if name == 'Ацетон':
        notes = [(days[3], 0.718, 'bo'), (days[6], 0.710, 'bo'), (days[7], 0.5065, 'bo'), (days[10], 0.391, 'bo')]
        return(days[:11], [0.661, 0.708, 0.728, 0.718, 0.702, 0.709, 0.710, 0.5065, 0.3830, 0.3865, 0.391], 0, 0.03, notes)
    if name == 'KOH':
        notes = []
        return (days, [0.733, 0.753, 0.762, 0.769, 0.772, 0.770, 0.775, 0.7741, 0.7588, 0.7591, 0.762, 0.755, 0.757, 0.764], 0, 0.03, notes)
    if name == 'H2SO4 конц.':
        notes = [(days[1], 1.551, 'ro')]
        return([0, 1], [0.887, 1.551], 0.1, 0, notes)
    if name == 'Морская вода':
        notes = []
        return(days, [0.593, 0.603, 0.613, 0.629, 0.6275, 0.623, 0.620, 0.651, 0.6217, 0.6184, 0.624, 0.627, 0.622, 0.627], 0, 0.022, notes)

list_of_ress = ['Ацетон', 'KOH', 'H2SO4 конц.', 'Морская вода']
for name in list_of_ress:
    x1, y1, move_x, move_y, notes = get_data(name)
    print(name)
    plt.plot(x1,y1) 
    plt.text(x1[0] + move_x, y1[0] + move_y, name)
    plt.plot(x1,y1, 'go') 
    for el in notes:
        plt.plot(el[0], el[1], el[2])
plt.plot(0, 1.9, 'ro')
plt.text(0.25, 1.88, '- Растворился')
plt.plot(0, 1.8, 'bo')
plt.text(0.25, 1.78, '- Отломился кусок')


    
plt.show()




