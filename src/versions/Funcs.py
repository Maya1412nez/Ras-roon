from PIL import Image
import numpy as np


def pairwise(iterable):
    a = iter(iterable)
    if len(iterable) % 2 == 1:
        a = iter(iterable + [None])
    return zip(a, a)

# l = [1, 2, 3, 4]
# for x, y in pairwise(l):
#    print(x, y)


def del_empty_rows(array):
    del_on_y = []
    for i in range(len(array)):
        if sum(array[i]) == 0:
            # differ for reas if we got > 1 rows fpr delling:
            # 0000 -> i = 0.       after del i == 0:
            # 0100 -> i = 1                             0100 -> i = 0
            # 0000 -> i = 2            -->              0000 -> i = 1 <- (1 = i - len(del_on_y - 1) = 2 - 1)
            del_on_y.append(i - len(del_on_y))
    for i in range(len(del_on_y)):
        array = np.delete(array, (del_on_y[i]), axis=0)
    return array


def del_empty_cols(array):
    found = []
    for j in range(len(array[0])):
        array_copy = array.copy()
        array = np.delete(array, (j), axis=1)  # delete each collum
        if sum(sum(array)) == sum(sum(array_copy)):  # was deleted colum with values != 0
            found.append(j)
        array = array_copy.copy()  # reverse matrix

    array = np.delete(array, (found), axis=1)
    return array


def get_upleft_index(mat, finding_value):
    left_ind_none = (99999999999999999999999, 999999999999999999999999999)
    left_ind = left_ind_none
    for i in range(len(mat)):
        if finding_value in mat[i]:
            left_ind = (i, (np.where(mat[i] == finding_value)[0][0]))
            break
    if left_ind == left_ind_none:
        return None
    return left_ind
    left_ind = int(left_ind[0]), int(left_ind[1])  # x, y


mat = np.array([
    [5, 2, 2, 0],
    [0, 2, 4, 0],
    [0, 9, 3, 0],
    [2, 1, 0, 5]
])
print(get_upleft_index(mat, 5))


def concatenate_images(image1, image0, side=None, step=0):
    from PIL import Image
    width, height, = image0.size
    width1, height1 = image1.size
    width, height = max(width, width1), max(height, height1)
    if side == 'up':
        new_image = Image.new('RGBA', (width, height * 2), (0, 0, 0, 0))
        new_image.paste(image0, (0, height - step), image0)
        new_image.paste(image1, (0, 0), image1)
        return new_image, (0, height - step)
    if side == 'down':
        new_image = Image.new('RGBA', (width, height * 2), (0, 0, 0, 0))
        new_image.paste(image0, (0, 0), image0)
        new_image.paste(image1, (0, height - step), image1)
        return new_image, (0, height - step)
    if side == 'left':
        new_image = Image.new('RGBA', (width * 2, height), (0, 0, 0, 0))
        new_image.paste(image0, (width - step, 0), image0)
        new_image.paste(image1, (0, 0), image1)
        return new_image, (width - step, 0)
    if side == 'right':
        new_image = Image.new('RGBA', (width * 2, height), (0, 0, 0, 0))
        new_image.paste(image0, (0, 0), image0)
        new_image.paste(image1, (width - step, 0), image1)
        return new_image, (width - step, 0)


# image1, image2 = Image.open('src/image/Image.png'), Image.open('src/image/dog.png')
# concatenate_images(image1, image2, right=1)

def best_concatenate_images(image_1, image_2):
    from Funcs import concatenate_images
    overlay = False
    sides = ['up', 'down', 'left', 'right']
    for side in sides:  # make best for each side
        if side == 'up' or side == 'down':
            side_for_matrix = 'y'
        else:
            side_for_matrix = 'x'
        obj_1 = image_to_obj(image_1)
        obj_2 = image_to_obj(image_2)
        good_obj, step = concatenate_matrixes(
            obj_1, obj_2, x, y, side=side_for_matrix)
        good_image, x, y = concatenate_images(image_1, image_2, side, step)
        good_obj.image.show
        good_obj.save_rez()


def image_to_obj(image):
    from Verse1_1_1 import MainImage
    obj = MainImage(its_image=image)
    obj.create_matrix()
    return obj


def concatenate_matrixes(obj1, obj2, x, y, sidik):
    data = {'x': x, 'y': y, 'matrix': obj2.matrix,
            'degrees': 'not that method, its concatenate'}
    obj1.add_images(data, side=sidik, step=1)
    step = obj1.summary_step
    return obj1
