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