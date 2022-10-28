stroka = input()
rast1 = 0
rast2 = 0
rast3 = 0
a = stroka.find("1")
rast1 += len(stroka) - a - 1
#print(stroka, rast1)
stroka = stroka[a + 1:]

b = stroka.find("1")
rast2 += len(stroka) - b - 1
print(stroka, rast2, b)
stroka1 = ''
if b > 1:
    for i in range(a + b - 1):
        stroka1 += '0'
    stroka1 += '10' + stroka
print('FF', stroka1)
rast_betwen = a
stroka = stroka[a + 1:]
print(stroka)

c = stroka.find("1")
rast3 += len(stroka) - c - 1
#print(stroka, rast3, c)
stroka = stroka[a + 1:]


