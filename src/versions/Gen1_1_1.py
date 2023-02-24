from Verse1_1_1 import MainImage, OverlayImage
from Gen0 import Individ, Population

def create_small_matrixes():
    MATRIX_QUANTITY = 3
    QUALITY = 2
    NAME = 'src/image/fork.png'
    OVER_IMAGE = OverlayImage(NAME)
    OVER_IMAGE.crop_image()
    WIDTH, HEIGHT = OVER_IMAGE.get_data()['width'], OVER_IMAGE.get_data()['height']
    WIDTH, HEIGHT = max(WIDTH, HEIGHT) * 2, max(WIDTH, HEIGHT) * 2
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
        MAIN_IMAGE.recreate_image()
        MAIN_IMAGE.save_rez(f'little_matrixs/little_matrix_2x2NUM{g}')
        # make_zones(MAIN_IMAGE)
        
# def make_zones(main_image_object):
#     for i in range(len(main_image_object.main_matrix)):
#         for j in range(len(main_image_object.main_matrix[i])):
#         #     print(main_image_object.main_matrix[i][j], end='')

#         # print()
#             pass


create_small_matrixes()
BESTIES = []
population = Population()
population.create_new()
    