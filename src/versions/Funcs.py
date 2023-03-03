import numpy as np

def pairwise(iterable):
    a = iter(iterable)
    if len(iterable) % 2 == 1:
        a = iter(iterable + [None])
    return zip(a, a)

# l = [1, 2, 3, 4]
# for x, y in pairwise(l):
#    print(x, y)

def del_empty_rows(array):
    del_on_y = []
    for i in range(len(array)):
        if sum(array[i]) == 0:
            # differ for reas if we got > 1 rows fpr delling:
            # 0000 -> i = 0.       after del i == 0:
            # 0100 -> i = 1                             0100 -> i = 0
            # 0000 -> i = 2            -->              0000 -> i = 1 <- (1 = i - len(del_on_y - 1) = 2 - 1)
            del_on_y.append(i - len(del_on_y))
    for i in range(len(del_on_y)):
        array = np.delete(array, (del_on_y[i]), axis=0)
    return array

def del_empty_cols(array):
    found = []
    for j in range(len(array[0])):
        array_copy = array.copy()
        array = np.delete(array, (j), axis=1) # delete each collum
        if sum(sum(array)) == sum(sum(array_copy)): # was deleted colum with values != 0
            found.append(j)
        array = array_copy.copy() # reverse matrix


    array = np.delete(array, (found), axis=1)
    return array 


def get_upleft_index(mat, finding_value):
    left_ind_none = (99999999999999999999999, 999999999999999999999999999)
    left_ind = left_ind_none
    for i in range(len(mat)):
        if finding_value in mat[i]:
            left_ind = (i, (np.where(mat[i] == finding_value)[0][0]))
            break
    if left_ind == left_ind_none:
        return None
    return left_ind
    left_ind = int(left_ind[0]), int(left_ind[1]) # x, y

mat = np.array([
    [5, 2, 2, 0],
    [0, 2, 4, 0],
    [0, 9, 3, 0],
    [2, 1, 0, 5]
])
print(get_upleft_index(mat, 5))

import numpy as np 
from matplotlib import pyplot as plt 
import collections

data_file = open('src/rezs/quality.txt', 'r', encoding='utf-8')
i = 0
x, x1 = [], []
y, y1 = [], []
s = 0
dict_x_y = dict()
for row in data_file:
    value = float(row.split()[9])
    x.append(i)
    y.append(value)
    i += 1
    s += int(row.split()[3])
    if not row.split()[3] in dict_x_y:
        dict_x_y[row.split()[3]] = []
    dict_x_y[row.split()[3]].append(value)
od = collections.OrderedDict(sorted(dict_x_y.items()))
print(od)
for x, y in od.items():
    x1.append(x)
    y1.append(sum(y) / len(y))
print(x1)
print(y1)


plt.title("Зависимость среднего качества от количества") 
plt.xlabel("коэфициент качества") 
plt.ylabel("количества") 
plt.plot(x1,y1) 
plt.show()