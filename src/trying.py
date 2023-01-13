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
ballons = []
n, m = map(int, input().split())
for i in range(n):
    ballons.append(set(map(int, input().split())))
if len(set.intersection(*ballons)) > 0:
    print(' '.join(map(str, sorted(list(set.intersection(*ballons))))))
else:
    print(-1)