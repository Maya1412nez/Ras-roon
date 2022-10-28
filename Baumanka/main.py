# def prost():
#     c = 0
#     f = 0
#     listik = [2]
#     listik2 = []
#     i = 1
#     while c < 21:
#         i += 1
#         f = 0
#         for el in listik:
#             if i % el == 0:
#                 f = 1
#         if f == 0:
#             listik.append(i)
#             c += 1
#             if i > 99:
#                 listik2.append(i)
#         # print(listik)
#     return listik
#
#
# print(prost())

# a, b, c = int(input()), int(input()), int(input())
# f = 0
# while f !
# f, f1, a, c = 0, 0, 0, 0
# n, m = int(input()), int(input())
# while f == 0:
#     a += 1
#     f1 = 0
#     b = 0
#     while f1 == 0:
#         b += 1
#         #print(f'a={a}, d={b} (он заплатит в сумме {a}+{n - 1}⋅{b}={a + (n - 1) * b} рубля)')
#         if m >= a + (n - 1) * b:
#             c += 1
#         else:
#             f1 = 1
#     if m < a + (n - 1):
#         # print(a + (n - 1))
#         f = 1
# print(c)


# import math
# def count(n, m):
#     f, f1, a, c = 0, 0, 0, 0
#     while m >= a + (n - 1):
#         a += 1
#         f += 1
#         b = 0
#         f1 = 0
#         while m >= a + (n - 1) * b:
#             b += 1
#             f1 += 1
#             print(f'a={a}, d={b} (он заплатит в сумме {a}+{n - 1}⋅{b}={a + (n - 1) * b} рубля)')
#             c += 1
#         c -= 1
#         print(f1 - 1)
#     print(f)
#     return c
#
#
# print(count(int(input()), int(input())))
# print(math.factorial(4))


f, f1, a, c = 0, 0, 0, 0
n, m = 6, 20
n1, m1 = n, m
c2 = 0
f3 = []
while f == 0:
    a += 1
    f1 = 0
    c1 = 0
    b = 0
    while f1 == 0:
        b += 1
        if m >= a + (n - 1) * b:
            print(f'a={a}, d={b} (он заплатит в сумме {a}+{n - 1}⋅{b}={a + (n - 1) * b} рубля)')
            c += 1
            c1 += 1
        else:
            f1 = 1
    print(c1)
    f3.append(c1)
    if m < a + (n - 1):
        # print(a + (n - 1))
        f = 1
    c2 += 1

m = m1
n = n1
f1=0
print(c2)
print(c)
print(f3)
print('dddddddddddd')
if m % 2 == 0:
    c = ((1 + (m / (n - 1) - 1)) / (n - 1) * (m / (n - 1) - 1)) * (n - 1)
else:
        c = ((1 + ((m - 1) / (n - 1) - 1)) / 2 * ((m - 1) / (n - 1) - 1)) * (n - 1) + ((m - 1) / (n - 1))
        if c == int(c):
            print(c)
print(c)
