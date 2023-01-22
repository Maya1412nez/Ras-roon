def pairwise(iterable):
    a = iter(iterable)
    if len(iterable) % 2 == 1:
        a = iter(iterable + [None])
    return zip(a, a)

l = [1, 2, 3, 4]

for x, y in pairwise(l):
   print(x, y)