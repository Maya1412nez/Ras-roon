# # # import matplotlib.pyplot as plt
# # # from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization! 
# # # from matplotlib import cm
# # # import numpy as np




# # # fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# # # ax = Axes3D(fig) #<-- Note the difference from your original code...

# # # x = np.arange(-10, 10, 0.25)
# # # y = np.arange(-10, 10, 0.25)
# # # x, y = np.meshgrid(x, y)
# # # a1 = [ i for i in range(-32, 33, 16)] * 5
# # # a2 = [ [i] * 5 for i in range(-32, 33, 16)]
# # # a2 = (sum(a2, []))
# # # z = 1 / (1 / 500 + (sum([1 / ((j + (x - a1[j]) ** 6) + (y - a2[j]** 6)) for j in range(1, 3)])) )
# # # # z = (1 - np.sin(np.sqrt(x ** 2 + y ** 2)) ** 2) / (1 + 0.001 * (x ** 2 + y ** 2))

# # # c = 0
# # # # for i in range(2):
# # # #     c += X[i] * np.sin(X[i] ** 0.5)
# # # # Z = 418.9829 - X * np.sin(X ** 0.5)
# # # # z = 0.5 * (x ** 2 + x * y + y ** 2) * (1  + 0.5 * np.cos(1.5 * x) * np.cos(3.2 * x * y) * np.cos(3.14 * y) + 0.5 * np.cos(2.2 * x) * np.cos(4.8 * x * y) * np.cos(3.5 * y))

# # # surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
# # #                        linewidth=0, antialiased=False)

# # # plt.show()
# # # l1 = []
# # # l = """(98, 'A'), (154, 'H'), (195, 'C'), (22, 'W'), (99, 'H'), (148, 'T'), (172, 'U'), (3, 'M'), (201, ']'), (112, 'F'), (202, ']'), (209, '2'), (63, '3'), (68, 'C'), (200, '='), (24, 'M'), (43, 'N'), (60, ';'), (206, '+'), (158, '>'), (105, 'S'), (18, 'H'), (189, 'K'), (2, 'R'), (4, 'N'), (88, 'Z'), (194, '8'), (130, 'N'), (139, '}'), (185, 'T'), (153, '&'), (147, 'U'), (210, 'O'), (75, '#'), (173, 'S'), (120, 'A'), (128, 'X'), (155, '"'), (90, '%'), (25, 'G'), (17, '/'), (20, '('), (32, 'J'), (86, 'F'), (19, '$'), (146, '9'), (159, '*'), (36, 'N'), (204, ':'), (13, '!'), (11, '2'), (162, '5'), (61, 'E'), (133, '3'), (192, 'M'), (152, 'U'), (96, 'M'), (0, 'Q'), (33, 'M'), (149, '['), (164, 'L'), (180, '6'), (23, ','), (12, 'E'), (57, 'F'), (121, '['), (191, 'U'), (14, '9'), (161, 'M'), (114, ':'), (29, 'M'), (166, 'W'), (125, 'V'), (205, 'L'), (49, '$'), (94, 'K'), (131, 'C'), (167, '_'), (82, 'V'), (115, 'T'), (138, '6'), (176, '#'), (59, '&'), (27, '.'), (9, '!'), (7, 'P'), (79, '#'), (107, 'R'), (111, 'N'), (54, 'U'), (198, 'T'), (123, 'U'), (109, '6'), (129, '<'), (134, 'P'), (178, 'W'), (157, '='), (56, 'V'), (44, 'S'), (186, '\\'), (64, '}'), (100, 'K'), (143, '3'), (132, '-'), (165, ';'), (207, 'I'), (160, 'K'), (106, 'O'), (47, '/'), (169, '('), (122, '3'), (119, 'G'), (144, 'U'), (91, 'J'), (174, 'S'), (170, 'D'), (6, 'Q'), (58, 'Z'), (87, '?'), (71, 'J'), (28, 'N'), (45, '8'), (182, '/'), (35, '`'), (84, 'Y'), (208, 'U'), (1, 'Q'), (199, '+'), (70, '}'), (108, 'T'), (177, '{'), (66, '6'), (69, 'J'), (10, '_'), (168, '('), (116, 'Y'), (175, 'I'), (183, 'X'), (110, '}'), (163, 'E'), (104, '1'), (74, 'Z'), (151, 'C'), (124, 'I'), (171, 'Y'), (97, 'X'), (184, ']'), (127, '<'), (103, '{'), (93, '7'), (81, 'V'), (117, 'H'), (34, 'D'), (52, '|'), (40, '2'), (193, '~'), (135, 'L'), (50, '|'), (145, '('), (41, '`'), (188, '_'), (190, ','), (67, 'R'), (179, '?'), (31, 'L'), (48, 'X'), (53, 'F'), (150, ','), (95, '1'), (55, 'T'), (126, '@'), (30, ')'), (137, '-'), (15, '@'), (92, 'G'), (101, 'E'), (203, 'S'), (78, '^'), (196, '+'), (136, '2'), (140, 'T'), (37, '!'), (51, '4'), (76, 'S'), (39, ';'), (73, 'Z'), (197, '^'), (113, 'F'), (65, '}'), (38, '_'), (118, '}'), (89, 'P'), (142, '"'), (156, 'I'), (26, '6'), (21, 'A'), (62, '\\'), (141, '>'), (181, 'H'), (102, 'Y'), (187, '3'), (46, '_'), (8, '+'), (42, '#'), (72, 'U'), (5, '$'), (16, '4'), (77, 'B'), (80, 'D'), (83, 'Y'), (85, 'A')"""
# # # l = list(l)
# # # for i in range(len(l)):
# # #     if l[i] == ',' and l[i - 1] != ')':
# # #         l[i] = ':'
# # # for i in range(len(l)):
# # #     if l[i] == ')' or l[i] == '(':
# # #         l[i] = ''
# # # #print(''.join(l))
# # # ll = {98: 'A', 154: 'H', 195: 'C', 22: 'W', 99: 'H', 148: 'T', 172: 'U', 3: 'M', 201: ']', 112: 'F', 202: ']', 209: '2', 63: '3', 68: 'C', 200: '=', 24: 'M', 43: 'N', 60: ';', 206: '+', 158: '>', 105: 'S', 18: 'H', 189: 'K', 2: 'R', 4: 'N', 88: 'Z', 194: '8', 130: 'N', 139: '}', 185: 'T', 153: '&', 147: 'U', 210: 'O', 75: '#', 173: 'S', 120: 'A', 128: 'X', 155: '"', 90: '%', 25: 'G', 17: '/', 20: '', 32: 'J', 86: 'F', 19: '$', 146: '9', 159: '*', 36: 'N', 204: ':', 13: '!', 11: '2', 162: '5', 61: 'E', 133: '3', 192: 'M', 152: 'U', 96: 'M', 0: 'Q', 33: 'M', 149: '[', 164: 'L', 180: '6', 23: ':', 12: 'E', 57: 'F', 121: '[', 191: 'U', 14: '9', 161: 'M', 114: ':', 29: 'M', 166: 'W', 125: 'V', 205: 'L', 49: '$', 94: 'K', 131: 'C', 167: '_', 82: 'V', 115: 'T', 138: '6', 176: '#', 59: '&', 27: '.', 9: '!', 7: 'P', 79: '#', 107: 'R', 111: 'N', 54: 'U', 198: 'T', 123: 'U', 109: '6', 129: '<', 134: 'P', 178: 'W', 157: '=', 56: 'V', 44: 'S', 186: '\'', 64: '}', 100: 'K', 143: '3', 132: '-', 165: ';', 207: 'I', 160: 'K', 106: 'O', 47: '/', 169: '', 122: '3', 119: 'G', 144: 'U', 91: 'J', 174: 'S', 170: 'D', 6: 'Q', 58: 'Z', 87: '?', 71: 'J', 28: 'N', 45: '8', 182: '/', 35: '`', 84: 'Y', 208: 'U', 1: 'Q', 199: '+', 70: '}', 108: 'T', 177: '{', 66: '6', 69: 'J', 10: '_', 168: '', 116: 'Y', 175: 'I', 183: 'X', 110: '}', 163: 'E', 104: '1', 74: 'Z', 151: 'C', 124: 'I', 171: 'Y', 97: 'X', 184: ']', 127: '<', 103: '{', 93: '7', 81: 'V', 117: 'H', 34: 'D', 52: '|', 40: '2', 193: '~', 135: 'L', 50: '|', 145: '', 41: '`', 188: '_', 190: ':', 67: 'R', 179: '?', 31: 'L', 48: 'X', 53: 'F', 150: ':', 95: '1', 55: 'T', 126: '@', 30: '', 137: '-', 15: '@', 92: 'G', 101: 'E', 203: 'S', 78: '^', 196: '+', 136: '2', 140: 'T', 37: '!', 51: '4', 76: 'S', 39: ';', 73: 'Z', 197: '^', 113: 'F', 65: '}', 38: '_', 118: '}', 89: 'P', 142: '"', 156: 'I', 26: '6', 21: 'A', 62: '\'', 141: '>', 181: 'H', 102: 'Y', 187: '3', 46: '_', 8: '+', 42: '#', 72: 'U', 5: '$', 16: '4', 77: 'B', 80: 'D', 83: 'Y', 85: 'A'}
# # # for el in ll:
# # #     l1.append(el)
# # # l1.sort()
# # # print('''

# # # ''')
# # # for el in l1:
# # #     print(ll[el], end='')
# # # print('''

# # # ''')

# # # import itertools
# # # ca = 0
# # # for c, el in enumerate(itertools.product("Кулебянки", repeat=6)):
# # #     s = ''.join(el)
# # #     if "бя" not in s and "уе" not in s and "уя" not in s and "уи" not in s and "еу" not in s and "яу" not in s and "иу" not in s:
# # #         if ('К' in s and s[0] == 'К') or 'К' not in s:
# # #             for j in range(6):
# # #                 co = list(s).count(j)
# # #                 if co > 1:
# # #                     break
# # #                 if co < 2 and j == 5:
# # #                     ca += 1
# # # print(ca)
# # # from time import sleep
# # # els = ['—', '\\', '|', '/']
# # # i = 0
# # # while True:
# # #     print(f'\r{els[i]}', end=' ')
# # #     if i == 3:
# # #         i = 0
# # #     else:
# # #         i += 1
# # #     sleep(0.2)

# # # values = list(map(int, input().split()))
# # # matrix = [['_' for _ in range(len(values) + 2)] for __ in range(max(values) + 3)]
# # # for i in range(len(matrix)):
# # #     for j in range(len(matrix[i])):
# # #         if i == 0 or i == (len(matrix) - 1) or j == 0 or j == (len(matrix[i])- 1):
# # #                 matrix[i][j] = '*'
# # #         # if i > 0 and i < len(matrix[i]) - 1:
# # #         #     print(i - 1, values, len(matrix) - values[i - 1] - 2, values[i - 1])
# # #         #if i > len(matrix) - values[i - 1] - 2:

# # #         elif j > 0 and j < len(matrix[i]) - 1 and i > 0 and i < len(matrix):
# # #             if i == len(matrix) - values[j]:
# # #                 matrix[i][j] = '='

# # # for j in range(len(matrix)):
# # #     print(''.join(matrix[j]))


# # # lst = input().split()
# # # maxx = ''
# # # for i in range(len(lst)):
# # #     if len(set(lst[i].upper())) > len(maxx):
# # #         maxx = lst[i]
# # # print(maxx)

# # # word = input()
# # # maxx = ''
# # # for el in (list(word)):
# # #     if not maxx or list(word).count(el) > (list(word)).count(max):
# # #         maxx = el
# # # print(maxx)

# # # sett1, sett2 = set(), set()

# # # for i in range(int(input())):
# # #     sett1.add(input())

# # # for i in range(int(input())):
# # #     sett2.add(input())
# # # dif = list(sett1.intersection(sett2))
# # # print()
# # # for i in range(len(sett1.intersection(sett2))):
# # #     print(dif[i])

# # # class A:
# # #     def met1(self):
# # #         print('No')
    
# # #     def met2(self):
# # #         self.met1()Z
# # # a = A()
# # # a.met2()
# # # import random
# # # lst = list(range(1, 50, 6))
# # # random.shuffle(list(range(1, 50, 6)))
# # # print(lst)

# # # num1, num2 = map(int, input().split())
# # # stroka1 = list(set(input().split()))
# # # stroka2 =  list(set(input().split()))
# # # for i in range(len(stroka1)):
# # #     if stroka1[i] in stroka2:
# # #         print('Yes')
# # #     else:
# # #         print('No')
# # # ballons = []
# # # n, m = map(int, input().split())
# # # for i in range(n):
# # #     ballons.append(set(map(int, input().split())))
# # # if len(set.intersection(*ballons)) > 0:
# # #     print(' '.join(map(str, sorted(list(set.intersection(*ballons))))))
# # # else:
# # #     print(-1)

# # # a, b, c = 5, 1, 6
# # # print([i for i in range(len([a, b, c])) if i in [max([a, b, c]), min([a, b, c])]])
# # # c = tuple(del [a, b, c][i for i in range(len([a, b, c])) if i not in [max([a, b, c]), min([a, b, c])])
# # # a, c = min(a, b, c), max(a, b, c)
# # # print(a, b, c)
# # # from random import choices
# # # IND_LENTH = 5
# # # params = [1, 0, 1, 0, 1]
# # # params = list(map(int, params))
# # # print(params)

# # # class LittleBell:
# # #     def sound(self):
# # #         print('ding')


# # # class Soda:
# # #     def __init__(self, adding=None) -> None:
# # #         self.adding = adding

# # #     def show_my_drink(self):
# # #         if self.adding:
# # #             print(f'Газировка и {self.adding}')
# # #         else:
# # #             print('Обычная газировка')


# # # class Nikola:
# # #     def __init__(self, name, age) -> None:
# # #         if name != 'Николай':
# # #             self.__name__ = "Я не {name}, а Николай"
# # #         else:
# # #             self.name = name
# # #         self.age = age


# # # class Sphere:
# # #     def __init__(self, rad=1, x=0, y=0, z=0) -> None:
# # #         self.radius = rad
# # #         self.x = x
# # #         self.y = y
# # #         self.z = z

# # #     def get_volume(self):
# # #         return 4/3 * 3.1415926 * self.radius ** 3

# # #     def get_square(self):
# # #         return 4 * 3.1415926 * self.radius

# # #     def get_radius(self):
# # #         return self.radius

# # #     def get_center(self):
# # #         return self.x, self.y, self.z

# # #     def set_radius(self, r):
# # #         self.radius = r
# # #         return None

# # #     def set_center(self, x, y, z):
# # #         self.x = x
# # #         self.y = y
# # #         self.z = z

# # #     def is_point_inside(self, x, y, z):
# # #         if x <= self.x + self.radius and y <= self.y + self.radius and z <= self.z + self.radius:
# # #             return True
# # #         return False


# # # soda = Soda()
# # # soda.show_my_drink()

# # # b = LittleBell
# # # b.sound()



# # # my_tuple = tuple(input(), list(map(int, input().split())), tuple(map(int, input().split())), tuple(map(int, input().split())))
# # # n = int(input())
# # # k  = int(input())

# # # print({1, 0} < {1, 2})

# # # s1, s2 = input(), input()
# # # k1, k2 = tuple(map(int, input().split())), tuple(map(int, input().split()))
# # # my_tuple_1 = ('Hello', (1, 2, 3, 4))
# # # my_tuple_2 = ('Hello', (1, 2))
# # # if my_tuple_1 > my_tuple_2:
# # #     print(my_tuple_1[0])
# # # elif my_tuple_2 > my_tuple_1:
# # #     print(my_tuple_2[1])
# # # else:
# # #     if my_tuple_1[1] > my_tuple_2[1]:
# # #         print(my_tuple_1[0])
# # #     else:
# # #         print(my_tuple_2[1])

# # a = [50, 41, 45, 12, 74, 56]
# # b = [13, 78, 50, 50, 46, 70, 90]
# # viborka = [a, b]
# # c, d = [], []
# # ab = a + b
# # for i in range(len(ab)):
# #     num = 2
# #     if ab[i] in a:
# #         num = 1
# #     c.append((ab[i], num))

# # c2 = sorted(c)

# # i, true_i = 1, 1
# # f = 0
# # item = None
# # new_num = None
# # while i <= len(ab):
# #     count = c2.count(c2[i- 1])
# #     if count > 1:
# #         item = c2[i- 1]
# #         if not new_num:
# #             new_num = (i * count + sum(j for j in range(count))) // count
# #     if c2[i- 1] == item:
# #         #print('yes')
# #         d.append(c2[i- 1] + (new_num, ))
# #     else:
# #         #print('no')
# #         new_num = None
# #         d.append(c2[i- 1] + (i, ))
# #     i += 1

# # print(d)

# # set_S = set()
# # min_viborka = min(viborka, key=len)
# # for i in range(len(d)):
# #     if d[i][0] in min_viborka:
# #         set_S.add(d[i][2])
# #         print(d[i])
# # S = sum(set_S)
# # print(S)

# # # S, f = 0, 2
# # # if len(a) <= len(b):
# # #     f = 1
# # # for i in range(len(d)):
# # #     if d[i][1] == f:
# # #         #print(d[i])
# # #         S += d[i][2]
# # # print(S)

# # parent1 = [0, 1, 2, 3, 4, 5, 6]
# # parent2 = ['00', 11, 22, 33, 44, 55, 66]
# # cut_place = 3
# # part1 = parent1[:cut_place]
# # part2 = parent2[cut_place:]
# # print(part1 + part2)


# def pairwise(iterable):
#     a = iter(iterable)
#     if len(iterable) % 2 == 1:
#         a = iter(iterable + [None])
#     return zip(a, a)

# l = [1, 2, 3, 4]

# for x, y in pairwise(l):
#    print(x, y)




# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QPainter
import sqlite3
from PIL import Image

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtGui import QIcon
from PIL import Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.my_counter = Management()
        self.face_im_name_num = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 50, 240, 50))
        self.comboBox.setObjectName("comboBox")

        # first face btn
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 30, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.counting_face_plus)
        self.pushButton.clicked.connect(self.im_face)

        # second face btn
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 50, 30, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.counting_face_minus)
        self.pushButton_2.clicked.connect(self.im_face)

        # first hair btn
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 130, 30, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.hair_im_name_num = 0
        self.pushButton_3.clicked.connect(self.counting_hair_plus)
        self.pushButton_3.clicked.connect(self.im_hair)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 130, 240, 50))
        self.comboBox_2.setObjectName("comboBox_2")

        # second hair btn
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 130, 30, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.counting_hair_minus)
        self.pushButton_4.clicked.connect(self.im_hair)

        # second eyes btn
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 210, 30, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.eyes_im_name_num = 0
        self.pushButton_5.clicked.connect(self.counting_eyes_minus)
        self.pushButton_5.clicked.connect(self.im_eyes)

        # first eyes btn
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 210, 30, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.counting_eyes_plus)
        self.pushButton_6.clicked.connect(self.im_eyes)

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(60, 210, 240, 50))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 240, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 240, 25))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 240, 25))
        self.label_3.setObjectName("label_3")

        # SAVE btn
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(840, 370, 100, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.saving)
        # добавить метод для сохранения изображения

        # first ears btn
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(20, 290, 30, 50))
        self.pushButton_14.setObjectName("pushButton_14")
        self.ears_im_name_num = 0
        self.pushButton_14.clicked.connect(self.counting_ears_plus)
        self.pushButton_14.clicked.connect(self.im_ears)

        # second ears btn
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(310, 290, 30, 50))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.counting_ears_minus)
        self.pushButton_15.clicked.connect(self.im_ears)

        self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_7.setGeometry(QtCore.QRect(60, 290, 240, 50))
        self.comboBox_7.setObjectName("comboBox_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 260, 240, 25))
        self.label_7.setObjectName("label_7")

        # first eyebrows btn
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(620, 50, 30, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.eyebrows_im_name_num = 0
        self.pushButton_7.clicked.connect(self.counting_eyebrows_plus)
        self.pushButton_7.clicked.connect(self.im_eyebrows)

        # first nose btn
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(620, 210, 30, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.nose_im_name_num = 0
        self.pushButton_8.clicked.connect(self.counting_nose_plus)
        self.pushButton_8.clicked.connect(self.im_nose)

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(660, 50, 240, 50))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_8.setGeometry(QtCore.QRect(660, 290, 240, 50))
        self.comboBox_8.setObjectName("comboBox_8")

        # first attribute btn
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(620, 290, 30, 50))
        self.pushButton_16.setObjectName("pushButton_16")
        self.attribute_im_name_num = 0
        self.pushButton_16.clicked.connect(self.counting_attribute_plus)
        self.pushButton_16.clicked.connect(self.im_attribute)

        # second mouth btn
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(910, 130, 30, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.mouth_im_name_num = 0
        self.pushButton_9.clicked.connect(self.counting_mouth_minus)
        self.pushButton_9.clicked.connect(self.im_mouth)

        # second nose btn
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(910, 210, 30, 50))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.counting_nose_minus)
        self.pushButton_10.clicked.connect(self.im_nose)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(660, 20, 240, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(660, 100, 240, 25))
        self.label_5.setObjectName("label_5")

        # second attribute btn
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(910, 290, 30, 50))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.counting_attribute_minus)
        self.pushButton_17.clicked.connect(self.im_attribute)

        # first mouth btn
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(620, 130, 30, 50))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.counting_mouth_plus)
        self.pushButton_11.clicked.connect(self.im_mouth)

        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(660, 210, 240, 50))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(660, 130, 240, 50))
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(660, 180, 240, 25))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(660, 260, 240, 25))
        self.label_8.setObjectName("label_8")

        # second eyebrows btn
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(910, 50, 30, 50))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.counting_eyebrows_minus)
        self.pushButton_12.clicked.connect(self.im_eyebrows)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # face
        self.mainlabel_face = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel_face.setGeometry(QtCore.QRect(360, 20, 240, 320))
        self.mainlabel_face.setObjectName("Main_Label")
        # вызов метода, отвечающей за инициализацию имени изображения
        # для этого - отдельный класс
        # переменная face_im_name создается в классе Management
        # self.face_im_name = 'sface1'
        # pixmap = QPixmap(f'imgs\{self.face_im_name}')
        # self.mainlabel_face.setPixmap(pixmap)

        # eyes
        self.mainlabel_eyes = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel_eyes.setGeometry(QtCore.QRect(360, 20, 240, 320))
        self.mainlabel_eyes.setObjectName("Main_Label")
        # вызов метода, отвечающей за инициализацию имени изображения
        # для этого - отдельный класс
        # self.eyes_im_name = "eyes3.png"
        # pixmap = QPixmap(f'imgs\{self.eyes_im_name}')
        # self.mainlabel_eyes.setPixmap(pixmap)

        # ears
        self.mainlabel_ears = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel_ears.setGeometry(QtCore.QRect(360, 20, 240, 320))
        self.mainlabel_ears.setObjectName("Main_Label")
        # вызов метода, отвечающей за инициализацию имени изображения
        # для этого - отдельный класс
        # self.ears_im_name = "ears3.png"
        # pixmap = QPixmap(f'imgs\{self.ears_im_name}')
        # self.mainlabel_ears.setPixmap(pixmap)

        # eyebrows
        self.mainlabel_eyebrows = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel_eyebrows.setGeometry(QtCore.QRect(360, 20, 240, 320))
        self.mainlabel_eyebrows.setObjectName("Main_Label")
        # вызов метода, отвечающей за инициализацию имени изображения
        # для этого - отдельный класс
        # self.eyebrows_im_name = "eyebrows3.png"
        # pixmap = QPixmap(f'imgs\{self.eyebrows_im_name}')
        # self.mainlabel_eyebrows.setPixmap(pixmap)

        # mouth
        self.mainlabel_mouth = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel_mouth.setGeometry(QtCore.QRect(360, 20, 240, 320))
        self.mainlabel_mouth.setObjectName("Main_Label")
        # вызов метода, отвечающей за инициализацию имени изображения
        # для этого - отдельный класс
        # self.mouth_im_name = "mouth1.png"
        # pixmap = QPixmap(f'imgs\{self.mouth_im_name}')
        # self.mainlabel_mouth.setPixmap(pixmap)

        # nose
        self.mainlabel_nose = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel_nose.setGeometry(QtCore.QRect(360, 20, 240, 320))
        self.mainlabel_nose.setObjectName("Main_Label")
        # вызов метода, отвечающей за инициализацию имени изображения
        # для этого - отдельный класс
        # self.nose_im_name = "snose1.png"
        # pixmap = QPixmap(f'imgs\{self.nose_im_name}')
        # self.mainlabel_nose.setPixmap(pixmap)

        # hair
        self.mainlabel_hair = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel_hair.setGeometry(QtCore.QRect(360, 20, 240, 320))
        self.mainlabel_hair.setObjectName("Main_Label")
        # вызов метода, отвечающего за инициализацию имени изображения
        # для этого - отдельный класс
        # self.hair_im_name = 'hair2.png'
        # pixmap = QPixmap(f'imgs\{self.hair_im_name}')
        # self.mainlabel_hair.setPixmap(pixmap)

        # attributes
        self.mainlabel_attribute = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel_attribute.setGeometry(QtCore.QRect(360, 20, 240, 320))
        self.mainlabel_attribute.setObjectName("Main_Label")
        # вызов метода, отвечающей за инициализацию имени изображения
        # для этого - отдельный класс
        # self.attribute_im_name = "attributes3.png"
        # pixmap = QPixmap(f'imgs\{self.attribute_im_name}')
        # self.mainlabel_attribute.setPixmap(pixmap)

        self.mainlabel_i = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel_i.setGeometry(QtCore.QRect(360, 20, 240, 320))
        self.mainlabel_i.setObjectName("Main_Label")
        # вызов метода, отвечающего за инициализацию имени изображения
        # для этого - отдельный класс
        # self.hair_im_name = 'hair2.png'
        pixmap = QPixmap('imgs\important.png')
        self.mainlabel_i.setPixmap(pixmap)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Мультяшный фоторобот"))
        self.pushButton.setText(_translate("MainWindow", "<"))
        self.pushButton_2.setText(_translate("MainWindow", ">"))
        self.pushButton_3.setText(_translate("MainWindow", "<"))
        self.pushButton_4.setText(_translate("MainWindow", ">"))
        self.pushButton_5.setText(_translate("MainWindow", ">"))
        self.pushButton_6.setText(_translate("MainWindow", "<"))
        self.label.setText(_translate("MainWindow", "Face"))
        self.label_2.setText(_translate("MainWindow", "Hair"))
        self.label_3.setText(_translate("MainWindow", "Eyes"))
        self.pushButton_13.setText(_translate("MainWindow", "Save"))
        self.pushButton_14.setText(_translate("MainWindow", "<"))
        self.pushButton_15.setText(_translate("MainWindow", ">"))
        self.label_7.setText(_translate("MainWindow", "Ears"))
        self.pushButton_7.setText(_translate("MainWindow", "<"))
        self.pushButton_8.setText(_translate("MainWindow", "<"))
        self.pushButton_16.setText(_translate("MainWindow", "<"))
        self.pushButton_9.setText(_translate("MainWindow", ">"))
        self.pushButton_10.setText(_translate("MainWindow", ">"))
        self.label_4.setText(_translate("MainWindow", "Eyebrows"))
        self.label_5.setText(_translate("MainWindow", "Mouth"))
        self.pushButton_17.setText(_translate("MainWindow", ">"))
        self.pushButton_11.setText(_translate("MainWindow", "<"))
        self.label_6.setText(_translate("MainWindow", "Nose"))
        self.label_8.setText(_translate("MainWindow", "Attributes"))
        self.pushButton_12.setText(_translate("MainWindow", ">"))

    def resize(self, param, param1):
        pass

    def counting_face_plus(self):
        self.face_im_name_num += 1
        p_of_n = 1
        self.num_face = int(str(p_of_n) + str(self.face_im_name_num % 3 + 1))
        self.face_im_name = self.my_counter.definition(self.num_face)
        print(self.face_im_name)

    def counting_face_minus(self):
        self.face_im_name_num -= 1
        p_of_n = 1
        self.num_face = int(str(p_of_n) + str(self.face_im_name_num % 3 + 1))
        self.face_im_name = self.my_counter.definition(self.num_face)
        print(self.face_im_name)

    def counting_hair_plus(self):
        p_of_n = 2
        self.hair_im_name_num += 1
        self.num_hair = int(str(p_of_n) + str(self.hair_im_name_num % 3 + 1))
        self.hair_im_name = self.my_counter.definition(self.num_hair)
        # self.face_im_name = self.my_counter.definition(self.num_face) докопировать эу строку в другие чести
        # print(self.hair_im_name)

    def counting_hair_minus(self):
        p_of_n = 2
        self.hair_im_name_num -= 1
        self.num_hair = int(str(p_of_n) + str(self.hair_im_name_num % 3 + 1))
        self.hair_im_name = self.my_counter.definition(self.num_hair)
        print(self.num_hair)

    def counting_ears_plus(self):
        p_of_n = 3
        self.ears_im_name_num += 1
        self.num_ears = int(str(p_of_n) + str(self.ears_im_name_num % 3 + 1))
        self.ears_im_name = self.my_counter.definition(self.num_ears)
        print(self.ears_im_name)

    def counting_ears_minus(self):
        p_of_n = 3
        self.ears_im_name_num -= 1
        self.num_ears = int(str(p_of_n) + str(self.ears_im_name_num % 3 + 1))
        self.ears_im_name = self.my_counter.definition(self.num_ears)
        print(self.ears_im_name)

    def counting_eyes_plus(self):
        p_of_n = 4
        self.eyes_im_name_num += 1
        self.num_eyes = int(str(p_of_n) + str(self.eyes_im_name_num % 3 + 1))
        self.eyes_im_name = self.my_counter.definition(self.num_eyes)
        print(self.eyes_im_name)

    def counting_eyes_minus(self):
        p_of_n = 4
        self.eyes_im_name_num -= 1
        self.num_eyes = int(str(p_of_n) + str(self.eyes_im_name_num % 3 + 1))
        self.eyes_im_name = self.my_counter.definition(self.num_eyes)
        print(self.eyes_im_name)

    def counting_eyebrows_plus(self):
        p_of_n = 5
        self.eyebrows_im_name_num += 1
        self.num_eyebrows = int(str(p_of_n) + str(self.eyebrows_im_name_num % 3 + 1))
        self.eyebrows_im_name = self.my_counter.definition(self.num_eyebrows)
        print(self.eyebrows_im_name)

    def counting_eyebrows_minus(self):
        p_of_n = 5
        self.eyebrows_im_name_num -= 1
        self.num_eyebrows = int(str(p_of_n) + str(self.eyebrows_im_name_num % 3 + 1))
        self.eyebrows_im_name = self.my_counter.definition(self.num_eyebrows)
        print(self.eyebrows_im_name)

    def counting_mouth_plus(self):
        p_of_n = 6
        self.mouth_im_name_num += 1
        self.num_mouth = int(str(p_of_n) + str(self.mouth_im_name_num % 3 + 1))
        self.mouth_im_name = self.my_counter.definition(self.num_mouth)
        print(self.mouth_im_name)

    def counting_mouth_minus(self):
        p_of_n = 6
        self.mouth_im_name_num -= 1
        self.num_mouth = int(str(p_of_n) + str(self.mouth_im_name_num % 3 + 1))
        self.mouth_im_name = self.my_counter.definition(self.num_mouth)
        print(self.mouth_im_name)

    def counting_nose_plus(self):
        p_of_n = 7
        self.nose_im_name_num += 1
        self.num_nose = int(str(p_of_n) + str(self.nose_im_name_num % 3 + 1))
        self.nose_im_name = self.my_counter.definition(self.num_nose)
        print(self.nose_im_name)

    def counting_nose_minus(self):
        p_of_n = 7
        self.nose_im_name_num -= 1
        self.num_nose = int(str(p_of_n) + str(self.nose_im_name_num % 3 + 1))
        self.nose_im_name = self.my_counter.definition(self.num_nose)
        print(self.nose_im_name)

    def counting_attribute_plus(self):
        p_of_n = 8
        self.attribute_im_name_num += 1
        self.num_attribute = int(str(p_of_n) + str(self.attribute_im_name_num % 3 + 1))
        self.attribute_im_name = self.my_counter.definition(self.num_attribute)
        print(self.attribute_im_name)

    def counting_attribute_minus(self):
        p_of_n = 8
        self.attribute_im_name_num -= 1
        self.num_attribute = int(str(p_of_n) + str(self.attribute_im_name_num % 3 + 1))
        self.attribute_im_name = self.my_counter.definition(self.num_attribute)
        print(self.attribute_im_name)

    def saving(self):
        img = Image.new('RGB', (240, 320))
        rez_face = Image.open(self.face_im_name.strip())
        rez_eyes = Image.open(f'imgs\{self.eyes_im_name.strip()}')
        rez_ears = Image.open(f'imgs\{self.ears_im_name.strip()}')
        rez_eyebrows = Image.open(f'imgs\{self.eyebrows_im_name.strip()}')
        rez_mouth = Image.open(f'imgs\{self.mouth_im_name.strip()}')
        rez_nose = Image.open(f'imgs\s{self.nose_im_name.strip()}')
        rez_hair = Image.open(f'imgs\{self.hair_im_name.strip()}')
        rez_attribute = Image.open(f'imgs\s{self.attribute_im_name.strip()}')
        img.paste(rez_face, (0, 0))
        img.paste(rez_eyes, (0, 0), rez_eyes)
        img.paste(rez_ears, (0, 0), rez_ears)
        img.paste(rez_eyebrows, (0, 0), rez_eyebrows)
        img.paste(rez_mouth, (0, 0), rez_mouth)
        img.paste(rez_nose, (0, 0), rez_nose)
        img.paste(rez_hair, (0, 0), rez_hair)
        img.paste(rez_attribute, (0, 0), rez_attribute)

        img.show()
        # прописать диалоговое окно для сохранения с вводом названия файла
        img.save("Durazkoe.jpg")

    def im_face(self):
        name = self.face_im_name.strip()
        print(self.face_im_name)
        pixmap = QPixmap(name)
        self.mainlabel_face.setPixmap(pixmap)

    def im_hair(self):
        name = self.hair_im_name.strip()
        print(self.hair_im_name) # не выводится
        pixmap = QPixmap(f'imgs\{name}')
        self.mainlabel_hair.setPixmap(pixmap)

    def im_eyes(self):
        name = self.eyes_im_name.strip()
        print(self.eyes_im_name) # не выводится
        pixmap = QPixmap(f'imgs\{name}')
        self.mainlabel_eyes.setPixmap(pixmap)

    def im_ears(self):
        name = self.ears_im_name.strip()
        print(self.ears_im_name) # не выводится
        pixmap = QPixmap(f'imgs\{name}')
        self.mainlabel_ears.setPixmap(pixmap)

    def im_eyebrows(self):
        name = self.eyebrows_im_name.strip()
        print(self.eyebrows_im_name) # не выводится
        pixmap = QPixmap(f'imgs\{name}')
        self.mainlabel_eyebrows.setPixmap(pixmap)

    def im_mouth(self):
        name = self.mouth_im_name.strip()
        print(self.mouth_im_name) # не выводится
        pixmap = QPixmap(f'imgs\{name}')
        self.mainlabel_mouth.setPixmap(pixmap)

    def im_nose(self):
        name = self.nose_im_name.strip()
        print(self.nose_im_name) # не выводится
        pixmap = QPixmap(f'imgs\s{name}')
        self.mainlabel_nose.setPixmap(pixmap)

    def im_attribute(self):
        name = self.attribute_im_name.strip()
        print(self.attribute_im_name) # не выводится
        pixmap = QPixmap(f'imgs\s{name}')
        self.mainlabel_attribute.setPixmap(pixmap)


class Management:
    def definition(self, num):
        self.data = open('data.txt', encoding='utf-8')
        self.image_name = None
        for row in self.data:
            row_l = row.split('*')
            number = row_l[0]
            if int(number) == num:
                self.image_name = row_l[1]
        self.data.close()
        # print(self.image_name)
        return self.image_name

        # self.image_name = f'{name}, {num}'
        # con = sqlite3.connect('image_base.sqlite')
        # cur = con.cursor()
        #
        # result = cur.execute("""SELECT * FROM imgs_name WHERE id like '21' """).fetchall()
        # con.close()
        #
        # for elem in result:
        #     print(elem[0])

        # if num == 1:
        #     self.name += 1
        # elif num == 0:
        #     self.name -= 1
        # else:
        #     print('defin.error')
        # self.rez = (self.name % 3) + 1
        # на основе одного из чисел counter определяется замена / добавление изображения
        # здесь же должна подключаться база данных, чтобы из нее брать названия изображений
        # имя counter + значение числа counter = id изображения
        # print(f'{name},{self.rez}')
        #
        # return f'{name},{self.rez}'
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())