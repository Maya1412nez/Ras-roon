import random
import numpy as np
import matplotlib

def f(x):
    return x * 2 + 3 + random.uniform(-0.1, 0.1)

def normal_f(x, k, b):
    return x * k + b
n = 10
m = 4
a, b = -5, 5
edu = []
test = []
edux = []
testx = []
for i in range(n):
    x = random.uniform(a, b)
    edux.append(x)
    edu.append(f(x))
edu = np.array(edu)
edux = np.array(edux)
for i in range(a, b):
    x = i
    testx.append(x)
    test.append(f(x))
test = np.array(test)
testx = np.array(testx)
print(test)

import matplotlib.pyplot as plt
plt.plot(edux, edu, 'ro')
plt.plot(testx, test, 'go')
plt.ylabel('some numbers')
print(testx)
print('--------------------------------------')
min_error = float("inf")
error = 0
best_k, best_b = 0, 0 
for k in range(-5, 5):
    for b in range(-5, 5):
        for i in range(len(testx)):
            x = testx[i]
            y = k*x + b 
            error += (abs(y - test[i]))
            print(y - test[i])
            # print(abs(y - test[i]))
        if error < min_error:
            min_error = error
            best_k, best_b = k, b
min_error

normal_y = normal_f(testx, best_k, best_b)
plt.plot(testx, normal_y)
plt.show()

