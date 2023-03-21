from Gen1_1_1 import create_small_matrixes, fight, create_children

QUANTITY = 128
QUALITY = 30
NAME = 'src/image/Image.png'
WIDTH, HEIGHT = 150, 150
FIGHTS = 4
GENERATIONS = 2

population = create_small_matrixes(NAME, QUANTITY, QUALITY, WIDTH, HEIGHT)
for g in range(GENERATIONS):
    print('--------------------------FIGHT--------------------------')
    for i in range(FIGHTS):
        population = fight(population)
    print('--------------------------CHILDREN--------------------------')
    population = create_children(population)


