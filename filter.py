from PIL import Image
import numpy as np


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
        if height_len % array[0] == 0 and width_len % array[0] == 0 and array[1] < 128:
            correct = False
            print('Данные корректы, ищите результат в папке.')
    return(array[0], array[1])


def choose_image():
    print('поместите в папку с проектом изображение, которое хотите переименовать, '
          '/n затем введите название через консоль')
    return input()


def search_grey(i, j, array, size, grad):
    sum = int(np.sum(array[i:i + size, j:j + size, 0]) + np.sum(array[i:i + size, j:j + size, 1])
              + np.sum(array[i:i + size, j:j + size, 2])) / 3
    total_grey = int(sum // (size * size))
    array[i:i + size, j:j + size, 0] = int(total_grey // grad) * grad
    array[i:i + size, j:j + size, 1] = int(total_grey // grad) * grad
    array[i:i + size, j:j + size, 2] = int(total_grey // grad) * grad


img = Image.open(choose_image())
pixel_array = np.array(img)
len_height = len(pixel_array)
len_width = len(pixel_array[1])
(size, gradient) = get_size_and_grad(len_height, len_width)
i = 0
while i < len_height:
    j = 0
    while j < len_width:
        search_grey(i, j, pixel_array, size, gradient)
        j = j + size
    i = i + size
res = Image.fromarray(pixel_array)
res.save('res.jpg')
