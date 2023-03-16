from Verse1_1_1 import MainImage, OverlayImage
from Funcs import pairwise

def create_small_matrixes():
    MATRIX_QUANTITY = 9
    QUALITY = 30
    list_of_objects = []
    NAME = 'src/image/Image.png'
    OVER_IMAGE = OverlayImage(NAME)
    OVER_IMAGE.crop_image()
    WIDTH, HEIGHT = OVER_IMAGE.get_data()['width'], OVER_IMAGE.get_data()['height']
    # WIDTH, HEIGHT = max(WIDTH, HEIGHT) * QUALITY, max(WIDTH, HEIGHT) * QUALITY
    WIDTH, HEIGHT = 100, 150
    list_of_objects = []
    print(f'WIDTH: {WIDTH}, HEIGHT: {HEIGHT}')


    for g in range(MATRIX_QUANTITY):
        MAIN_IMAGE = MainImage(WIDTH, HEIGHT)
        print(f'-----------------little_matrix_2x2NUM{g}-----------------')
        for t in range(QUALITY):
            # all changes. check that everyone is here
            OVER_IMAGE = OverlayImage(NAME)
            OVER_IMAGE.crop_image()
            OVER_IMAGE.edit_random(WIDTH, HEIGHT)
            OVER_IMAGE.create_matrix()
            OVER_IMAGE.save_rez()
            # all changes. check that everyone is here
            datas = OVER_IMAGE.get_data()
            MAIN_IMAGE.add_images(datas, numbers=1)
        MAIN_IMAGE.crop_matrix()
        # MAIN_IMAGE.recreate_image()
        MAIN_IMAGE.save_rez(f'little_matrixs/little_matrix_2x2NUM{g}')
        list_of_objects.append(MAIN_IMAGE)
        # make_zones(MAIN_IMAGE)
<<<<<<< Updated upstream
    return list_of_objects

        
=======
        list_of_objects.append(MAIN_IMAGE)
    return list_of_objects
>>>>>>> Stashed changes
# def make_zones(main_image_object):
#     for i in range(len(main_image_object.main_matrix)):
#         for j in range(len(main_image_object.main_matrix[i])):
#         #     print(main_image_object.main_matrix[i][j], end='')

#         # print()
#             pass


list_of_objects = create_small_matrixes()
BESTIES = []

<<<<<<< Updated upstream

def fight(list_of_objects):
    # for i in range(len(list_of_objects)):
        # print((((IMAGE.get_quality()).split())[-1])[:5])
    winner_list = []
    order = [i for i in range(len(list_of_objects))]
    for i, j in pairwise(order):
            winner = local_fight(list_of_objects, i, j)
            print('winner:', (((winner.get_quality()).split())[-1])[:5])
            winner_list.append(winner)
            winner.image.save(f'src/rezs/winners/{i}.png')


        
def local_fight(list_of_objects, i, j):
    if j != None:
        first_figter, second_fighter = list_of_objects[i], list_of_objects[j]
        print('fighters:', (((first_figter.get_quality()).split())[-1])[:5], (((second_fighter.get_quality()).split())[-1])[:5])
        if first_figter.get_quality() > second_fighter.get_quality():
            return first_figter
        return second_fighter
    return list_of_objects[i]
    
print('--------------------------FIGHT--------------------------')
fight(list_of_objects)
=======
def fight():
    for i in range(len(list_of_objects)):
        IMAGE = list_of_objects[i]
        print(IMAGE.)
>>>>>>> Stashed changes
