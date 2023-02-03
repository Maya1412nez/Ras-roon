from Verse1_1_1 import MainImage, OverlayImage

def create_small_matrixes():
    MATIX_QUANTITY = 4
    QUALITY = 2
    NAME = 'src/image/dog.png'
    OVER_IMAGE = OverlayImage(NAME)
    OVER_IMAGE.crop()
    WIDTH, HEIGHT = OVER_IMAGE.get_data()['width'], OVER_IMAGE.get_data()['height']
    WIDTH, HEIGHT = max(WIDTH, HEIGHT) * 2, max(WIDTH, HEIGHT) * 2
    print(f'WIDTH: {WIDTH}, HEIGHT: {HEIGHT}')


    for g in range(MATIX_QUANTITY):
        MAIN_IMAGE = MainImage(WIDTH, HEIGHT)
        print(f'-----------------little_matrix_2x2NUM{g}-----------------')
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
        MAIN_IMAGE.crop()
        MAIN_IMAGE.save_rez(f'little_matrixs/little_matrix_2x2NUM{g}')
