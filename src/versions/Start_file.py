
from Verse1_1_1 import MainImage, OverlayImage
WIDTH, HEIGHT = 800, 500
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
    MAIN_IMAGE.save_rez()