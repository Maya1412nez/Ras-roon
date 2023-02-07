# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization! 
# from matplotlib import cm
# import numpy as np




# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax = Axes3D(fig) #<-- Note the difference from your original code...

# x = np.arange(-10, 10, 0.25)
# y = np.arange(-10, 10, 0.25)
# x, y = np.meshgrid(x, y)
# a1 = [ i for i in range(-32, 33, 16)] * 5
# a2 = [ [i] * 5 for i in range(-32, 33, 16)]
# a2 = (sum(a2, []))
# z = 1 / (1 / 500 + (sum([1 / ((j + (x - a1[j]) ** 6) + (y - a2[j]** 6)) for j in range(1, 3)])) )
# # z = (1 - np.sin(np.sqrt(x ** 2 + y ** 2)) ** 2) / (1 + 0.001 * (x ** 2 + y ** 2))

# c = 0
# # for i in range(2):
# #     c += X[i] * np.sin(X[i] ** 0.5)
# # Z = 418.9829 - X * np.sin(X ** 0.5)
# # z = 0.5 * (x ** 2 + x * y + y ** 2) * (1  + 0.5 * np.cos(1.5 * x) * np.cos(3.2 * x * y) * np.cos(3.14 * y) + 0.5 * np.cos(2.2 * x) * np.cos(4.8 * x * y) * np.cos(3.5 * y))

# surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)

# plt.show()
# l1 = []
# l = """(98, 'A'), (154, 'H'), (195, 'C'), (22, 'W'), (99, 'H'), (148, 'T'), (172, 'U'), (3, 'M'), (201, ']'), (112, 'F'), (202, ']'), (209, '2'), (63, '3'), (68, 'C'), (200, '='), (24, 'M'), (43, 'N'), (60, ';'), (206, '+'), (158, '>'), (105, 'S'), (18, 'H'), (189, 'K'), (2, 'R'), (4, 'N'), (88, 'Z'), (194, '8'), (130, 'N'), (139, '}'), (185, 'T'), (153, '&'), (147, 'U'), (210, 'O'), (75, '#'), (173, 'S'), (120, 'A'), (128, 'X'), (155, '"'), (90, '%'), (25, 'G'), (17, '/'), (20, '('), (32, 'J'), (86, 'F'), (19, '$'), (146, '9'), (159, '*'), (36, 'N'), (204, ':'), (13, '!'), (11, '2'), (162, '5'), (61, 'E'), (133, '3'), (192, 'M'), (152, 'U'), (96, 'M'), (0, 'Q'), (33, 'M'), (149, '['), (164, 'L'), (180, '6'), (23, ','), (12, 'E'), (57, 'F'), (121, '['), (191, 'U'), (14, '9'), (161, 'M'), (114, ':'), (29, 'M'), (166, 'W'), (125, 'V'), (205, 'L'), (49, '$'), (94, 'K'), (131, 'C'), (167, '_'), (82, 'V'), (115, 'T'), (138, '6'), (176, '#'), (59, '&'), (27, '.'), (9, '!'), (7, 'P'), (79, '#'), (107, 'R'), (111, 'N'), (54, 'U'), (198, 'T'), (123, 'U'), (109, '6'), (129, '<'), (134, 'P'), (178, 'W'), (157, '='), (56, 'V'), (44, 'S'), (186, '\\'), (64, '}'), (100, 'K'), (143, '3'), (132, '-'), (165, ';'), (207, 'I'), (160, 'K'), (106, 'O'), (47, '/'), (169, '('), (122, '3'), (119, 'G'), (144, 'U'), (91, 'J'), (174, 'S'), (170, 'D'), (6, 'Q'), (58, 'Z'), (87, '?'), (71, 'J'), (28, 'N'), (45, '8'), (182, '/'), (35, '`'), (84, 'Y'), (208, 'U'), (1, 'Q'), (199, '+'), (70, '}'), (108, 'T'), (177, '{'), (66, '6'), (69, 'J'), (10, '_'), (168, '('), (116, 'Y'), (175, 'I'), (183, 'X'), (110, '}'), (163, 'E'), (104, '1'), (74, 'Z'), (151, 'C'), (124, 'I'), (171, 'Y'), (97, 'X'), (184, ']'), (127, '<'), (103, '{'), (93, '7'), (81, 'V'), (117, 'H'), (34, 'D'), (52, '|'), (40, '2'), (193, '~'), (135, 'L'), (50, '|'), (145, '('), (41, '`'), (188, '_'), (190, ','), (67, 'R'), (179, '?'), (31, 'L'), (48, 'X'), (53, 'F'), (150, ','), (95, '1'), (55, 'T'), (126, '@'), (30, ')'), (137, '-'), (15, '@'), (92, 'G'), (101, 'E'), (203, 'S'), (78, '^'), (196, '+'), (136, '2'), (140, 'T'), (37, '!'), (51, '4'), (76, 'S'), (39, ';'), (73, 'Z'), (197, '^'), (113, 'F'), (65, '}'), (38, '_'), (118, '}'), (89, 'P'), (142, '"'), (156, 'I'), (26, '6'), (21, 'A'), (62, '\\'), (141, '>'), (181, 'H'), (102, 'Y'), (187, '3'), (46, '_'), (8, '+'), (42, '#'), (72, 'U'), (5, '$'), (16, '4'), (77, 'B'), (80, 'D'), (83, 'Y'), (85, 'A')"""
# l = list(l)
# for i in range(len(l)):
#     if l[i] == ',' and l[i - 1] != ')':
#         l[i] = ':'
# for i in range(len(l)):
#     if l[i] == ')' or l[i] == '(':
#         l[i] = ''
# #print(''.join(l))
# ll = {98: 'A', 154: 'H', 195: 'C', 22: 'W', 99: 'H', 148: 'T', 172: 'U', 3: 'M', 201: ']', 112: 'F', 202: ']', 209: '2', 63: '3', 68: 'C', 200: '=', 24: 'M', 43: 'N', 60: ';', 206: '+', 158: '>', 105: 'S', 18: 'H', 189: 'K', 2: 'R', 4: 'N', 88: 'Z', 194: '8', 130: 'N', 139: '}', 185: 'T', 153: '&', 147: 'U', 210: 'O', 75: '#', 173: 'S', 120: 'A', 128: 'X', 155: '"', 90: '%', 25: 'G', 17: '/', 20: '', 32: 'J', 86: 'F', 19: '$', 146: '9', 159: '*', 36: 'N', 204: ':', 13: '!', 11: '2', 162: '5', 61: 'E', 133: '3', 192: 'M', 152: 'U', 96: 'M', 0: 'Q', 33: 'M', 149: '[', 164: 'L', 180: '6', 23: ':', 12: 'E', 57: 'F', 121: '[', 191: 'U', 14: '9', 161: 'M', 114: ':', 29: 'M', 166: 'W', 125: 'V', 205: 'L', 49: '$', 94: 'K', 131: 'C', 167: '_', 82: 'V', 115: 'T', 138: '6', 176: '#', 59: '&', 27: '.', 9: '!', 7: 'P', 79: '#', 107: 'R', 111: 'N', 54: 'U', 198: 'T', 123: 'U', 109: '6', 129: '<', 134: 'P', 178: 'W', 157: '=', 56: 'V', 44: 'S', 186: '\'', 64: '}', 100: 'K', 143: '3', 132: '-', 165: ';', 207: 'I', 160: 'K', 106: 'O', 47: '/', 169: '', 122: '3', 119: 'G', 144: 'U', 91: 'J', 174: 'S', 170: 'D', 6: 'Q', 58: 'Z', 87: '?', 71: 'J', 28: 'N', 45: '8', 182: '/', 35: '`', 84: 'Y', 208: 'U', 1: 'Q', 199: '+', 70: '}', 108: 'T', 177: '{', 66: '6', 69: 'J', 10: '_', 168: '', 116: 'Y', 175: 'I', 183: 'X', 110: '}', 163: 'E', 104: '1', 74: 'Z', 151: 'C', 124: 'I', 171: 'Y', 97: 'X', 184: ']', 127: '<', 103: '{', 93: '7', 81: 'V', 117: 'H', 34: 'D', 52: '|', 40: '2', 193: '~', 135: 'L', 50: '|', 145: '', 41: '`', 188: '_', 190: ':', 67: 'R', 179: '?', 31: 'L', 48: 'X', 53: 'F', 150: ':', 95: '1', 55: 'T', 126: '@', 30: '', 137: '-', 15: '@', 92: 'G', 101: 'E', 203: 'S', 78: '^', 196: '+', 136: '2', 140: 'T', 37: '!', 51: '4', 76: 'S', 39: ';', 73: 'Z', 197: '^', 113: 'F', 65: '}', 38: '_', 118: '}', 89: 'P', 142: '"', 156: 'I', 26: '6', 21: 'A', 62: '\'', 141: '>', 181: 'H', 102: 'Y', 187: '3', 46: '_', 8: '+', 42: '#', 72: 'U', 5: '$', 16: '4', 77: 'B', 80: 'D', 83: 'Y', 85: 'A'}
# for el in ll:
#     l1.append(el)
# l1.sort()
# print('''

# ''')
# for el in l1:
#     print(ll[el], end='')
# print('''

# ''')

# import itertools
# ca = 0
# for c, el in enumerate(itertools.product("Кулебянки", repeat=6)):
#     s = ''.join(el)
#     if "бя" not in s and "уе" not in s and "уя" not in s and "уи" not in s and "еу" not in s and "яу" not in s and "иу" not in s:
#         if ('К' in s and s[0] == 'К') or 'К' not in s:
#             for j in range(6):
#                 co = list(s).count(j)
#                 if co > 1:
#                     break
#                 if co < 2 and j == 5:
#                     ca += 1
# print(ca)
# from time import sleep
# els = ['—', '\\', '|', '/']
# i = 0
# while True:
#     print(f'\r{els[i]}', end=' ')
#     if i == 3:
#         i = 0
#     else:
#         i += 1
#     sleep(0.2)

# values = list(map(int, input().split()))
# matrix = [['_' for _ in range(len(values) + 2)] for __ in range(max(values) + 3)]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i == 0 or i == (len(matrix) - 1) or j == 0 or j == (len(matrix[i])- 1):
#                 matrix[i][j] = '*'
#         # if i > 0 and i < len(matrix[i]) - 1:
#         #     print(i - 1, values, len(matrix) - values[i - 1] - 2, values[i - 1])
#         #if i > len(matrix) - values[i - 1] - 2:

#         elif j > 0 and j < len(matrix[i]) - 1 and i > 0 and i < len(matrix):
#             if i == len(matrix) - values[j]:
#                 matrix[i][j] = '='

# for j in range(len(matrix)):
#     print(''.join(matrix[j]))


# lst = input().split()
# maxx = ''
# for i in range(len(lst)):
#     if len(set(lst[i].upper())) > len(maxx):
#         maxx = lst[i]
# print(maxx)

# word = input()
# maxx = ''
# for el in (list(word)):
#     if not maxx or list(word).count(el) > (list(word)).count(max):
#         maxx = el
# print(maxx)

# sett1, sett2 = set(), set()

# for i in range(int(input())):
#     sett1.add(input())

# for i in range(int(input())):
#     sett2.add(input())
# dif = list(sett1.intersection(sett2))
# print()
# for i in range(len(sett1.intersection(sett2))):
#     print(dif[i])

# class A:
#     def met1(self):
#         print('No')
    
#     def met2(self):
#         self.met1()Z
# a = A()
# a.met2()
# import random
# lst = list(range(1, 50, 6))
# random.shuffle(list(range(1, 50, 6)))
# print(lst)

# num1, num2 = map(int, input().split())
# stroka1 = list(set(input().split()))
# stroka2 =  list(set(input().split()))
# for i in range(len(stroka1)):
#     if stroka1[i] in stroka2:
#         print('Yes')
#     else:
#         print('No')
# ballons = []
# n, m = map(int, input().split())
# for i in range(n):
#     ballons.append(set(map(int, input().split())))
# if len(set.intersection(*ballons)) > 0:
#     print(' '.join(map(str, sorted(list(set.intersection(*ballons))))))
# else:
#     print(-1)

# a, b, c = 5, 1, 6
# print([i for i in range(len([a, b, c])) if i in [max([a, b, c]), min([a, b, c])]])
# c = tuple(del [a, b, c][i for i in range(len([a, b, c])) if i not in [max([a, b, c]), min([a, b, c])])
# a, c = min(a, b, c), max(a, b, c)
# print(a, b, c)
# from random import choices
# IND_LENTH = 5
# params = [1, 0, 1, 0, 1]
# params = list(map(int, params))
# print(params)

# class LittleBell:
#     def sound(self):
#         print('ding')


# class Soda:
#     def __init__(self, adding=None) -> None:
#         self.adding = adding

#     def show_my_drink(self):
#         if self.adding:
#             print(f'Газировка и {self.adding}')
#         else:
#             print('Обычная газировка')


# class Nikola:
#     def __init__(self, name, age) -> None:
#         if name != 'Николай':
#             self.__name__ = "Я не {name}, а Николай"
#         else:
#             self.name = name
#         self.age = age


# class Sphere:
#     def __init__(self, rad=1, x=0, y=0, z=0) -> None:
#         self.radius = rad
#         self.x = x
#         self.y = y
#         self.z = z

#     def get_volume(self):
#         return 4/3 * 3.1415926 * self.radius ** 3

#     def get_square(self):
#         return 4 * 3.1415926 * self.radius

#     def get_radius(self):
#         return self.radius

#     def get_center(self):
#         return self.x, self.y, self.z

#     def set_radius(self, r):
#         self.radius = r
#         return None

#     def set_center(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def is_point_inside(self, x, y, z):
#         if x <= self.x + self.radius and y <= self.y + self.radius and z <= self.z + self.radius:
#             return True
#         return False


# soda = Soda()
# soda.show_my_drink()

# b = LittleBell
# b.sound()



# my_tuple = tuple(input(), list(map(int, input().split())), tuple(map(int, input().split())), tuple(map(int, input().split())))
# n = int(input())
# k  = int(input())

# print({1, 0} < {1, 2})

# s1, s2 = input(), input()
# k1, k2 = tuple(map(int, input().split())), tuple(map(int, input().split()))
# my_tuple_1 = ('Hello', (1, 2, 3, 4))
# my_tuple_2 = ('Hello', (1, 2))
# if my_tuple_1 > my_tuple_2:
#     print(my_tuple_1[0])
# elif my_tuple_2 > my_tuple_1:
#     print(my_tuple_2[1])
# else:
#     if my_tuple_1[1] > my_tuple_2[1]:
#         print(my_tuple_1[0])
#     else:
#         print(my_tuple_2[1])

# a = [50, 41, 45, 12, 74, 56]
# b = [13, 78, 50, 50, 46, 70, 90]
# viborka = [a, b]
# c, d = [], []
# ab = a + b
# for i in range(len(ab)):
#     num = 2
#     if ab[i] in a:
#         num = 1
#     c.append((ab[i], num))

# c2 = sorted(c)

# i, true_i = 1, 1
# f = 0
# item = None
# new_num = None
# while i <= len(ab):
#     count = c2.count(c2[i- 1])
#     if count > 1:
#         item = c2[i- 1]
#         if not new_num:
#             new_num = (i * count + sum(j for j in range(count))) // count
#     if c2[i- 1] == item:
#         #print('yes')
#         d.append(c2[i- 1] + (new_num, ))
#     else:
#         #print('no')
#         new_num = None
#         d.append(c2[i- 1] + (i, ))
#     i += 1

# print(d)

# set_S = set()
# min_viborka = min(viborka, key=len)
# for i in range(len(d)):
#     if d[i][0] in min_viborka:
#         set_S.add(d[i][2])
#         print(d[i])
# S = sum(set_S)
# print(S)

# S, f = 0, 2
# if len(a) <= len(b):
#     f = 1
# for i in range(len(d)):
#     if d[i][1] == f:
#         #print(d[i])
#         S += d[i][2]
# print(S)



# cache = dict()

# def factorial(n):
#     if n in cache:
#         return cache[n]
#     if n == 1:
#         res = 1
#         cache[n] = res
#         return res
#     else:
#         res = factorial(n - 1) * n
#         cache[n] = res
#         return res

# # print(factorial(5))
# # print(cache)

# def f(n):
#     if n in cache:
#         return cache[n]
#     if n <= 2:
#         cache[n] = n
#         return n
#     cache[n] = n * (n - 1) + f(n - 1) + f(n - 2)
#     return n * (n - 1) + f(n - 1) + f(n - 2)

# for i in range(2023):
#     f(i)
# print(f(2023) - f(2021) - 2 * f(2020) - f(2019))

# def f(n):
#     if n in cache:
#         return cache[n]
#     if n == 0:
#         cache[n] = 0
#         return 0
#     elif n % 2 == 1:
#         res = f(n - 1) + 1
#         cache[n] = res
#         return res
#     else:
#         res = f(n / 2)
#         cache[n] = res
#         return res
# count = 0
# # for i in range(1000000000):
# #     a = f(i)
# #     if a == 3:
# #         count += 1
# print(f(254))
# a = '125 101 115 114 101 118 110 105 123 89 69 75'
# s = a.split()
# print(s)
# for i in range(len(s)):
#     print(chr(int(s[i])), end='')


# cache = {}
# def f(n):
#     if n in cache:
#         return cache[n]
#     if n <= 2:
#         res = 1
#         cache[n] = res
#         return res
#     else:
#         res = n + f(n - 3) + f(n - 42)
#         cache[n] = res
#         return res

# for i in range(2023):
#     f(i)
# a = f(2023) + f(2021) - 2 * f(213)
# a1 = list(map(int, list(str(a))))
# print(sum(a1))
# <?xml version="1.0" encoding="UTF-8" standalone="no"?>

# <?xml version="1.0" encoding="UTF-8" standalone="no"?>
# <svg version="1.0" xmlns:svg="http://www.w3.org/2000/svg"
#    xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" x="0px" y="0px" width="120px" height="120px">
#     <path d="M 110.6133 3.8057 L 85.3066 26.5962 L 72.3525 49.686 L 60 49.9863 L 47.6475 49.686 L 34.6929 26.5962 L 9.3877 3.8057 L 15.2617 35.5933 L 35.2964 58.5332 L 31.2295 74.5742 L 32.8843 94.2168 L 39.0615 100.3633 L 42.5259 108.7607 L 52.4678 115.959 L 59.9795 112.9668 L 57.7627 107.085 L 52.4678 101.0781 L 60 104.877 L 67.5313 101.0781 L 62.2383 107.085 L 60.0205 112.9668 L 67.5313 115.959 L 77.4727 108.7607 L 80.9365 100.3633 L 87.1143 94.2168 L 88.7705 74.5742 L 84.7031 58.5332 L 104.7383 35.5933 L 110.6133 3.8057 Z" fill="#cecece"></path>
# </svg>
# from random import choices, shuffle, randint

# params = choices(['0', '1'], k=10)
# print(''.join(params))
# print((int(''.join(params), 2)))


# import numpy as np

# # x = np.linspace(-5, 5, 11)
# # print(x)
# # x = np.array([1, 2, 3])
# # print(x)

# # for item in x:
# #     print(item)

# y = np.array([7,1, 9])
# x = list(set(y))
# if len(x) == 1 and len(y) > 1:
#     mm = x[0]
# else:
#     m, mm = None, None
#     for i in range(len(x)):
#         if m == None:
#             m, mm = x[i], None
#         else:
#             if x[i] < m:
#                 mm = m
#                 m = x[i]
#             elif x[i] > m:
#                 if mm == None:
#                     mm = x[i]
#                 else:
#                     if mm > x[i]:
#                         mm = x[i]
# print(mm)

# from Verse1_1_2 import OverlayImage
# im1 = OverlayImage('src/image/dog.png')
# print(im1.height, im1.width)
# im1.crop()
# print(im1.height, im1.width)

# im1.create_matrix()
# im1.save_rez()
# im2 = OverlayImage('src/image/dog1.png')
# im2.crop()
# im2.create_matrix()
# im2.save_rez()

# for row in im1.matrix:
#     print(row)
# print('''





# ''')
# for row in im2.matrix:
#     print(row)
# print(im1.matrix == im2.matrix)
# print(len(im1.matrix), len(im1.matrix[0]))
# import numpy as np
# c = 0
# for i in np.arange(1, 101, 0.5):
#     c += i
# print(c)

from time import sleep

r = 150
for i in range(r + 1):
    n = i // 10
    s = ""
    for j in range(n):
        s += "="
        sleep(0.01)
    s = "="*n + "-"*((r // 10)-n)
    print(f"\x1b[32m \r DONE: {i} from {r}   [{s}]'\x1b[0m", end='')



