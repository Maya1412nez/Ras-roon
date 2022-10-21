import copy
from random import randint, choice

from PIL import Image


class MainImage:
    def __init__(self, width, height):
        self.main_width = width
        self.main_height = height
        self.main_image = Image.new('RGB', (self.main_width, self.main_height), (0, 0, 0, 0))
        self.main_demo_image = Image.new('RGB', (self.main_width, self.main_height), (118, 255, 97))
        self.main_matrix = [[0 for _ in range(self.main_width)] for __ in range(self.main_height)]

    def add_images(self, data):
        print(data)
        overlaying_image = Image.open('rezs/ready_image.png')
        x, y, over_matrix = data
        ov_im_width, ov_im_height = overlaying_image.size
        good_height = False
        im_qual = 0
        fail_count = 0

        while not good_height and y >= 0:
            matrix_copy = copy.deepcopy(self.main_matrix)
            overlay = False
            for i in range(self.main_height):
                for j in range(self.main_width):
                    # ENTER
                    small_i = i - y
                    small_j = j - x
                    if ov_im_height > small_i >= 0 and ov_im_width > small_j >= 0:
                        if not self.main_matrix[i][j] == over_matrix[small_i][small_j] == 1:
                            self.main_matrix[i][j] = over_matrix[small_i][small_j]

                        else:
                            overlay = True
            if not overlay:
                self.main_image.paste(overlaying_image, (x, y), overlaying_image)
                good_height = True
                im_qual += 1
                # fail_count = 0
            else:
                fail_count += 1

                self.main_matrix = matrix_copy
                y -= 10

        print('DONE!')

    def save_rez(self):
        self.main_image.save('rezs/main_image.png')
        print(*self.main_matrix, sep='\n')


class OverlayImage:
    def __init__(self, image_name):
        self.image = Image.open(image_name)
        self.width, self.height = self.image.size
        self.x, self.y = 0, 0

        print(f'''Start image size:
                Width: {self.width} Height: {self.height}''')
        self.demo_image = Image.new('RGB', (self.width, self.height),
                                    (118, 255, 97))
        self.demo_image.paste(self.image, (0, 0), self.image)
        self.pixels = self.image.load()
        self.matrix = [[0] * self.width for _ in range(self.height)]  # создание матрицы с нулями

    def crop(self):
        image_square = 0
        lower_right_coord = [None, None]  # lower right - L
        upper_left_coord = [None, None]  # upper left - U:
        # _  _  U  _  _  1  _  _  _  _  _
        # _  _  _  _  _  1  _  _  _  _  _
        # _  _  1  2  3  4  5  6  7  _  _
        # _  _  1  _  _  2  _  _  3  _  _
        # _  _  1  _  _  2  _  _  L  _  _

        for i in range(self.width):
            for j in range(self.height):
                r, g, b, a = self.pixels[i, j]
                if a != 0:
                    # -----------------------------
                    image_square += 1
                    # -----------------------------
                    if upper_left_coord[0] is None:
                        upper_left_coord[0] = i
                    if upper_left_coord[1] is None:
                        upper_left_coord[1] = j

                    if lower_right_coord[0] is None:
                        lower_right_coord[0] = i
                    if lower_right_coord[1] is None:
                        lower_right_coord[1] = j
                    else:
                        if upper_left_coord[0] > i:
                            upper_left_coord = i
                        if upper_left_coord[1] > j:
                            upper_left_coord[1] = j

                        if lower_right_coord[0] < i:
                            lower_right_coord[0] = i
                        if lower_right_coord[1] < j:
                            lower_right_coord[1] = j
                    # -----------------------------

        print((f'''New coords:
                        Upper Left point: {upper_left_coord[0], upper_left_coord[1]};
                        Lower right point: {lower_right_coord[0], lower_right_coord[1]}
            '''))
        print(f'''Square of PNG im (in pixels): {image_square}
            ''')
        # -------RESULTING--------

        # ---maximum possible quality of small images in big main image---
        possible_quality = (1200 * 700) // image_square
        self.demo_image = self.demo_image.crop(
            (upper_left_coord[0], upper_left_coord[1], lower_right_coord[0], lower_right_coord[1]))
        self.image = self.image.crop(
            (upper_left_coord[0], upper_left_coord[1], lower_right_coord[0], lower_right_coord[1]))
        print(f'''Possible quality: {possible_quality}''')

    def save_rez(self):
        self.image.save('rezs/image.png')
        self.demo_image.save('rezs/demo_image.png')

    def edit_random(self, main_image_width, main_image_height):
        flip_degrees = [0, 90, 180, 270]  # список градусов поворота
        degrees = choice(flip_degrees)  # выбор градуса поворота

        self.image = self.image.rotate(degrees, expand=True)  # поворот PNG изображения
        self.demo_image = self.demo_image.rotate(
            degrees,
            expand=True)  # поворот того же изображения, но наложенного на зеленый фон (r = 118 and g = 255 and b = 97)
        self.width, self.height = self.image.size  # переопределение размеров
        print(self.image.size)
        self.x, self.y = (randint(0, main_image_width - self.width)), (main_image_height - self.height)
        print(self.x, self.y)
        # x, y = 10, (self.main_image_height - self.height)
        print(
            f'''New random coordinates: {self.x, self.y}
                New random flip degrees: {degrees}
                ''')
        self.pixels = self.image.load()

    def create_matrix(self):
        # check pixels, matrix
        for i in range(self.height):
            for j in range(self.width):
                r, g, b, a = self.pixels[j, i]
                if a != 0:  # if pix != None
                    self.matrix[i][j] = 1  # замена 0 на 1

    def get_data(self):
        # return f'{self.image} {self.x} {self.y} {self.matrix}'
        self.image.save('rezs/ready_image.png')
        return self.x, self.y, self.matrix


w, h = 500, 300
quality = 6
name = 'image/Image.png'

main_image = MainImage(w, h)

for t in range(quality):
    # all changes. check that everyone is here
    over_image = OverlayImage(name)
    over_image.crop()
    over_image.edit_random(w, h)
    over_image.create_matrix()
    over_image.save_rez()
    # all changes. check that everyone is here
    datas = over_image.get_data()
    main_image.add_images(datas)
main_image.save_rez()
