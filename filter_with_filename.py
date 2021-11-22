from PIL import Image
import numpy as np
import doctest

def get_size_and_grad(height_len, width_len):
    correct = True
    flag = 0
    while correct:
        if flag > 0:
            print("размеру мозаики должен быть делителем для ширины и высоты изображения, "
                  "а градация серого должна быть меньше 128")
        print('Введите размер мозаики и градацию серого через  пробел: ')
        flag += 1
        array = input().split(' ')
        array = [int(x) for x in array]
        if correct_values(height_len, width_len, array[0], array[1]):
            correct = False
            print('Данные корректы, ищите результат в папке.')
    return(array[0], array[1])


def correct_values(hlen, wlen, size, grad):
    """
    >>> correct_values(750, 750, 25, 260)
    False
    >>> correct_values(750, 750, 31, 15)
    False
    """
    return hlen % size == 0 and wlen % size == 0 and grad < 128


def choose_image():
    print('поместите в папку с проектом изображение, которое хотите переименовать, '
          'затем введите название через консоль')
    return input()


def search_grey(i, j, array, size):
    """
    >>> search_grey(0, 0, np.array(Image.open('img2.jpg')), 5)
    19
    """
    sum = int(np.sum(array[i:i + size, j:j + size, 0]) + np.sum(array[i:i + size, j:j + size, 1])
              + np.sum(array[i:i + size, j:j + size, 2])) / 3
    return int(sum // (size * size))


def change_quarter(i, j, array, size, grad, total_grey):
    array[i:i + size, j:j + size, 0] = int(total_grey // grad) * grad
    array[i:i + size, j:j + size, 1] = int(total_grey // grad) * grad
    array[i:i + size, j:j + size, 2] = int(total_grey // grad) * grad


img = Image.open('img2.jpg')
pixel_array = np.array(img)
len_height = len(pixel_array)
len_width = len(pixel_array[1])
(size, gradient) = (10, 50)
i = 0
while i < len_height:
    j = 0
    while j < len_width:
        total_grey = search_grey(i, j, pixel_array, size)
        change_quarter(i, j, pixel_array, size, gradient, total_grey)
        j = j + size
    i = i + size
res = Image.fromarray(pixel_array)
res.save('res.jpg')
doctest.testmod()