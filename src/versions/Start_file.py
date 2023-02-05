
from Verse1_1_2 import MainImage, OverlayImage
WIDTH, HEIGHT = 200, 100
QUALITY = 2
NAME = 'src/image/dog.png'

MAIN_IMAGE = MainImage(WIDTH, HEIGHT)

for t in range(QUALITY):
    # all changes. check that everyone is here
    OVER_IMAGE = OverlayImage(NAME)
    OVER_IMAGE.crop()
    OVER_IMAGE.edit_random(WIDTH, HEIGHT)
    OVER_IMAGE.create_matrix()
    OVER_IMAGE.save_rez()
    # all changes. check that everyone is here
    datas = OVER_IMAGE.get_data()
    MAIN_IMAGE.add_images(datas)
    MAIN_IMAGE.save_rez(name='1')
MAIN_IMAGE.recheck()
# print(MAIN_IMAGE.height, MAIN_IMAGE.last_i, MAIN_IMAGE.width, MAIN_IMAGE.last_j)
MAIN_IMAGE.save_rez(name='2')
print('the work is completed'.upper())
