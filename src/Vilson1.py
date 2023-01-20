a = [50, 41, 45, 12, 74, 56]
b = [13, 78, 50, 50, 46, 70, 90]
viborka = [a, b]
c, d = [], []
ab = a + b
for i in range(len(ab)):
    num = 2
    if ab[i] in a:
        num = 1
    c.append((ab[i], num))

c2 = sorted(c)

i, true_i = 1, 1
f = 0
item = None
new_num = None
while i <= len(ab):
    count = c2.count(c2[i- 1])
    if count > 1:
        item = c2[i- 1]
        if not new_num:
            new_num = (i * count + sum(j for j in range(count))) // count
    if c2[i- 1] == item:
        #print('yes')
        d.append(c2[i- 1] + (new_num, ))
    else:
        #print('no')
        new_num = None
        d.append(c2[i- 1] + (i, ))
    i += 1

print(d)

set_S = set()
min_viborka = min(viborka, key=len)
for i in range(len(d)):
    if d[i][0] in min_viborka:
        set_S.add(d[i][2])
        print(d[i])
S = sum(set_S)
print(S)