# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

min1 = [0, array[0]]
max1 = [0, array[0]]

for index, val in enumerate(array):
    if min1[1] >= val:
        min1[0] = index
        min1[1] = val
    if max1[1] <= val:
        max1[0] = index
        max1[1] = val
print(f'Минимальный элемент = {min1[1]} | Максимальный элемент = {max1[1]}')
print(f'До заменты =  {array}')
array[min1[0]], array[max1[0]] = array[max1[0]], array[min1[0]]
print(f'После заменты = {array}')
