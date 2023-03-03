import numpy as np 
from matplotlib import pyplot as plt 
import collections

def make_range(name, a=0):
    data_file = open(f'src/rezs/{name}', 'r', encoding='utf-8')
    i = 0
    x, x1 = [], []
    y, y1 = [], []
    dict_x_y = dict()
    for row in data_file:
        value = float(row.split()[9])
        x.append(i)
        y.append(value)
        i += 1
        if not row.split()[3] in dict_x_y:
            dict_x_y[int(row.split()[3])] = []
        dict_x_y[int(row.split()[3])].append(value)
    list_of_keys = sorted(dict_x_y)
    print(1111111111111111, list_of_keys)
    od = collections.OrderedDict(sorted(dict_x_y.items()))

    for x, y in od.items():
        x1.append(x)
        if a:
            y1.append(sum(y) / len(y) + (x - 10) / 10)
        else:
            y1.append(sum(y) / len(y))
        print(sum(y), len(y))
    return x1, y1

plt.title("Зависимость среднего качества от количества") 
plt.xlabel("количество фигур") 
plt.ylabel("коэфициент качества") 
list_of_ress = ['Quality_tetris.txt', 'Plus_evolution.txt', 'Dirty_table.txt']
for name in list_of_ress:
    a = 0
    if name == 'Plus_evolution.txt':
        a = 1
    x1, y1 = make_range(name, a=a)
    plt.plot(x1,y1) 
plt.show()