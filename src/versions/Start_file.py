
from Verse1_1_4 import MainImage, OverlayImage
from time import sleep

WIDTH, HEIGHT = 400, 300
QUALITY = 70
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
    MAIN_IMAGE.save_rez(name='imp/1')
    for j in range((t // 10)):
        s += "="
        sleep(0.01)
    s = "="*(t // 10) + "-"*((QUALITY // 10)-(t // 10))
    print(f"\x1b[32m \r \r DONE: {t} from {QUALITY}   [{s}]'\x1b[0m", end='')
MAIN_IMAGE.recheck()
# MAIN_IMAGE.a()
# print(MAIN_IMAGE.height, MAIN_IMAGE.last_i, MAIN_IMAGE.width, MAIN_IMAGE.last_j)
MAIN_IMAGE.save_rez(name='imp/2')
print('the work is completed'.upper())


