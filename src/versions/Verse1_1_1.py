# -*- coding: utf-8 -*-
import copy
from random import randint, choice
import time
from PIL import Image
import numpy as np
from Funcs import del_empty_cols, del_empty_rows, get_upleft_index


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
        # создание матрицы с нулями
        self.matrix = np.zeros((self.height, self.width))
        self.degrees = None

    def crop_image(self):
        image_square = 0
        self.width, self.height = self.image.size
        self.pixels = self.image.load()
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
            (upper_left_coord[0], upper_left_coord[1], lower_right_coord[0] +1, lower_right_coord[1] +1))
        print(f'''Possible quality: {possible_quality}''')
        self.width, self.height = self.image.size  # переопределение размеров
        print(f'new width: {self.width}, new_height: {self.height}')

    def save_rez(self, name=None):
        if name == None:
            self.image.save('src/rezs/image.png')
            self.demo_image.save('src/rezs/demo_image.png')
        # else:
        #     self.image.save(f'src/rezs/{name}.png')
        #     self.demo_image.save(f'src/rezs/{name}.png')

    def set_parametr(self, degr=None):
        if degr:
            self.degrees = degr
            self.image = self.image.rotate(self.degrees, expand=True)  # поворот PNG изображения

    def edit_random(self, main_image_width, main_image_height):
        flip_degrees = [0, 90, 180, 270]  # список градусов поворота
        self.degrees = choice(flip_degrees)  # выбор градуса поворота

        self.image = self.image.rotate(
            self.degrees, expand=True)  # поворот PNG изображения
        self.demo_image = self.demo_image.rotate(
            self.degrees,
            expand=True)  # поворот того же изображения, но наложенного на зеленый фон (r = 118 and g = 255 and b = 97)
        self.width, self.height = self.image.size  # переопределение размеров
        print(self.image.size)
        self.x, self.y = (randint(0, main_image_width - self.width)
                          ), (main_image_height - self.height)
        print(self.x, self.y)
        # x, y = 10, (self.main_image_height - self.height)
        print(
            f'''New random coordinates: {self.x, self.y}
                New random flip degrees: {self.degrees}
                ''')
        self.pixels = self.image.load()

    def create_matrix(self):
        # check pixels, matrix
        self.pixels = self.image.load()
        for i in range(self.height):
            for j in range(self.width):
                r, g, b, a = self.pixels[j, i]
                if a != 0:  # if pix != None
                    self.matrix[i][j] = 1  # замена 0 на 1

    def get_data(self):
        # return f'{self.image} {self.x} {self.y} {self.matrix}'
        self.image.save('src/rezs/ready_image.png')
        rez = dict()
        rez['x'] = self.x
        rez['y'] = self.y
        rez['height'] = self.height
        rez['matrix'] = self.matrix
        rez['width'] = self.width
        rez['degrees'] = self.degrees
        return rez


class MainImage(OverlayImage):
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.image = Image.new(
            'RGBA', (self.width, self.height), (0, 0, 0, 0))
        self.demo_image = Image.new(
            'RGBA', (self.width, self.height), (118, 255, 97))
        self.main_matrix = np.zeros((self.height, self.width))
        self.pixels = self.image.load()
        # if we want to numerize each image in matix, one of imgs'll be with "1", anohter with "2" and etc
        self.numbers_for_matrix = 1
        self.dict_of_numbers_and_degrees = {}
        self.coords = []
        self.file_name = name

    def add_images(self, data, numbers=False):
        overlaying_image = Image.open('src/rezs/ready_image.png')
        x, y, over_matrix, degrees = data['x'], data['y'], data['matrix'], data['degrees']
        ov_im_width, ov_im_height = overlaying_image.size
        good_height = False
        im_qual = 0
        fail_count = 0
        self.coords.append((y, x))

        while not good_height and y >= 0:
            matrix_copy = copy.deepcopy(self.main_matrix)
            overlay = False
            # over_matrix[0][0] =  -self.numbers_for_matrix # helping marks
            # helping marks
            # over_matrix[ov_im_height - 1][ov_im_width - 1] = -self.numbers_for_matrix 
            for i in range(self.height):
                for j in range(self.width):
                    # ENTER
                    small_i = i - y
                    small_j = j - x
                    # Be careful when reading matrix with marks!!
                    if ov_im_height > small_i >= 0 and ov_im_width > small_j >= 0:
                        # be careful there
                        if not self.main_matrix[i][j] >= over_matrix[small_i][small_j] == 1:
                            if self.main_matrix[i][j] == 0:
                                if over_matrix[small_i][small_j] > 0:
                                        self.main_matrix[i][j] = self.numbers_for_matrix

                        else:
                            overlay = True
            if not overlay:
                self.image.paste(
                    overlaying_image, (x, y), overlaying_image)
                good_height = True
                im_qual += 1
                # fail_count = 0
                if numbers:
                        self.dict_of_numbers_and_degrees[self.numbers_for_matrix] = degrees
                        self.numbers_for_matrix += 1
            else:
                fail_count += 1

                self.main_matrix = matrix_copy
                y -= 10

        print('DONE!')

        # self.main_image.show()
        # print(*self.main_matrix, sep='\n')
        # time.sleep(3)

    def save_rez(self, name=None):
        if name == None:
            self.image.save('src/rezs/main_image_from_1.1.1.png')
            # print(*self.main_matrix, sep='\n')
            file = open('src/rezs/rezult_1.1.1.txt', 'w', encoding='utf-8')
        else:
            self.image.save(f'src/rezs/{name}.png')
            # print(*self.main_matrix, sep='\n')
            file = open(f'src/rezs/{name}.txt', 'w', encoding='utf-8')

        for row in self.main_matrix:
            np.set_printoptions(linewidth=2000)
            file.write(f'[{str(row)}],')
            # print(row)
            file.write('\n')
        file.write(str(self.dict_of_numbers_and_degrees))
        # print(self.main_matrix)

    def recreate_image(self):
        self.crop_image()
        self.width, self.height = len(self.main_matrix), len(self.main_matrix[0])
        print(f'NEW WIDTH {self.width} NEW HEIGHT {self.height}')
        self.image = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        print(888888888888888888, self.dict_of_numbers_and_degrees)
        for number, degrees in self.dict_of_numbers_and_degrees.items():
            print(f'NUMBER: {number}, DEGREES: {degrees}')
            print(get_upleft_index(self.main_matrix, number))
            over_image = OverlayImage(self.file_name)
            over_image.crop_image()
            over_image.set_parametr(degr=degrees)
            over_image.image.show()



    def check_quality(self): # this method for delling wrong matrixes with few elements
        for matix_num, degrees in self.dict_of_numbers_and_degrees.items():
            if get_upleft_index(self.main_matrix, matix_num) == None:
                pass 
            

    # def recreate_matrix(self):
    #     for i in range(len(self.main_matrix)):
    #         if sum(self.main_matrix[i]) == 0:
    #             self.main_matrix = self.main_matrix[1:]
    #     for j in range(len(self.main_matrix[0])):
    #         pass

    def crop_matrix(self):
        self.image.crop()
        self.width, self.height = self.image.size  # переопределение размеров
        self.main_matrix = del_empty_rows(self.main_matrix)
        self.main_matrix = del_empty_cols(self.main_matrix)
        if len(self.main_matrix) != self.width or len(self.main_matrix[0]) != self.height:
            print('IMAGE != MATRIX!!!!')
            print('make coord for second image on matrix and refactor image, using this coords, width, height, etc')
# WIDTH, HEIGHT = 800, 500
# QUALITY = 200
# NAME = 'src/image/dog.png'

# MAIN_IMAGE = MainImage(WIDTH, HEIGHT)

# for t in range(QUALITY):
#     # all changes. check that everyone is here
#     OVER_IMAGE = OverlayImage(NAME)
#     OVER_IMAGE.crop()
#     OVER_IMAGE.edit_random(WIDTH, HEIGHT)
#     OVER_IMAGE.create_matrix()
#     OVER_IMAGE.save_rez()
#     # all changes. check that everyone is here
#     datas = OVER_IMAGE.get_data()
#     MAIN_IMAGE.add_images(datas)
#     MAIN_IMAGE.save_rez()
