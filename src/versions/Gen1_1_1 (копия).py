from Verse1_1_1 import MainImage, OverlayImage
from Funcs import pairwise, concatenate_images
from time import sleep
from random import *

def create_small_matrixes():
    MATRIX_QUANTITY = 4
    QUALITY = 30
    NAME = 'src/image/Image.png'
    OVER_IMAGE = OverlayImage(NAME)
    OVER_IMAGE.crop_image()
    WIDTH, HEIGHT = OVER_IMAGE.get_data()['width'], OVER_IMAGE.get_data()['height']
    # WIDTH, HEIGHT = max(WIDTH, HEIGHT) * QUALITY, max(WIDTH, HEIGHT) * QUALITY
    WIDTH, HEIGHT = 150, 150
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
    return list_of_objects

        
# def make_zones(main_image_object):
#     for i in range(len(main_image_object.main_matrix)):
#         for j in range(len(main_image_object.main_matrix[i])):
#         #     print(main_image_object.main_matrix[i][j], end='')

#         # print()
#             pass


list_of_objects = create_small_matrixes()

BESTIES = []


def fight(list_of_objects):
    # for i in range(len(list_of_objects)):
        # print((((IMAGE.get_quality()).split())[-1])[:5])
    winner_list = []
    order = [i for i in range(len(list_of_objects))]
    shuffle(order)
    for i, j in pairwise(order):
            winner = local_fight(list_of_objects, i, j)
            print('winner:', (((winner.get_quality()).split())[-1])[:5])
            winner_list.append(winner)
            winner.image.save(f'src/rezs/winners/{i}.png')
    print('---------------END_OF_POPULATION---------------')
    return winner_list


        
def local_fight(list_of_objects, i, j):
    if j != None:
        first_figter, second_fighter = list_of_objects[i], list_of_objects[j]
        print('fighters:', (((first_figter.get_quality()).split())[-1])[:5], (((second_fighter.get_quality()).split())[-1])[:5])
        if first_figter.get_quality() > second_fighter.get_quality():
            return first_figter
        return second_fighter
    return list_of_objects[i]
    
print('--------------------------FIGHT--------------------------')
i = 0
while len(list_of_objects) > 10 or i < 1:
    list_of_objects = fight(list_of_objects)
    print(len(list_of_objects))
    # sleep(10)
    i += 1

def create_children(list_of_parents):
    children_list = []
    order = [i for i in range(len(list_of_objects))]
    shuffle(order)
    for i, j in pairwise(order):
        child = create_child(list_of_parents, i, j)
        child.create_matrix()
        child.save_rez(f'/children/{i}')
        children_list.append(child)
        child.image.show()


def create_child(list_of_parents, i, j, side=None):
    parent1_obj, parent2_obj = list_of_parents[i], list_of_parents[j]
    parent1_image, parent2_image = parent1_obj.image, parent2_obj.image
    parent1_image.show()
    parent2_image.show()
    child_image_up = concatenate_images(parent1_image, parent2_image, side='up')[0]
    child_image_down = concatenate_images(parent1_image, parent2_image, side='down')[0]
    child_image_right = concatenate_images(parent1_image, parent2_image, side='right')[0]
    child_image_left = concatenate_images(parent1_image, parent2_image, side='left')[0]

    child_obj_up = MainImage(its_image=child_image_up)
    child_obj_down = MainImage(its_image=child_image_down)
    child_obj_right = MainImage(its_image=child_image_right)
    child_obj_left = MainImage(its_image=child_image_left)

    quality_up = child_obj_up.get_quality()
    quality_down = child_obj_down.get_quality()
    quality_right = child_obj_right.get_quality()
    quality_left = child_obj_left.get_quality()
    
    if side == 'up':
        return child_obj_up
    elif side == 'down':
        return child_obj_down
    elif side == 'right':
        return child_obj_right
    elif side == 'left':
        return child_obj_left

    if max([quality_up, quality_down, quality_right, quality_left]) == quality_up:
        return child_obj_up
    if max([quality_up, quality_down, quality_right, quality_left]) == quality_down:
        return child_obj_down
    if max([quality_up, quality_down, quality_right, quality_left]) == quality_right:
        return child_obj_right
    return child_obj_left

create_children(list_of_objects)