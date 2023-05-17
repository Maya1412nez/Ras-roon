# import random
# import numpy as np
# def f(x):
#     return x * 2 + 3 + random.uniform(-0.1, 0.1)

# a, b = -5, 5
# n = 10
# edu = []
# edux = []
# m = 4
# test = []
# testx = []
# for i in range(n):
#     x = random.uniform(a, b)
#     edux.append(x)
#     edu.append(f(x))
# edu = np.array(edu)
# for i in range(m):
#     x = random.uniform(a, b)
#     testx.append(x)
#     test.append(f(x))
# test = np.array(test)
# print(edu)
# print(test)
# #.........
# def y(x, k, c):
#     return k*x+c

# min_e = None
# min_k = None
# min_c = None
# for k in np.arange(-5, 5, 0.01):
#     for c in np.arange(-5, 5, 0.01):
#         e = 0
#         for item in edu:
#             e += (edux[i]-y(edu[i], k, c))**2
#         e = (e/len(edu))**0.5
#         if min_e is None or e < min_e:
#             min_e = e
#             min_k = k
#             min_c = c
# print(min_e, min_k, min_c)

# import matplotlib.pyplot as plt
# plt.plot(edux, edu, 'ro')
# plt.plot(testx, test, 'go')
# plt.ylabel('some numbers')
# plt.show()

import random
import numpy as np
def f(x):
    return 6 / (x + 3) # + random.uniform(-0.1, 0.1)

a, b = 1, 6
n = 10
edu = []
m = 4
test = []
edux = []
testx = []
for i in range(n):
    x = random.uniform(a, b)
    edux.append(x)
    edu.append(f(x))
edu = np.array(edu)
for i in range(m):
    x = random.uniform(a, b)
    testx.append(x)
    test.append(f(x))
test = np.array(test)
#print(edu)
#print(test)
#.........
def y(x, k, c):
    return k / (x + c)

min_e = None
min_k = None
min_c = None
for k in np.arange(-5, 5, 0.01):
    for c in np.arange(-5, 5, 0.01):
        e = 0
        for item in edu:
            e += (edu[i]-y(edux[i], k, c))**2
        e = (e/len(edu))**0.5
        if min_e is None or e < min_e:
            min_e = e
            min_k = k
            min_c = c
print(min_e, min_k, min_c)

import matplotlib.pyplot as plt
plt.plot(edux, edu)
plt.plot(edux, edu, 'ro')
t = sorted(test)
tx = sorted(testx)
plt.plot(t, tx, 'go')
plt.ylabel('some numbers')
plt.show()