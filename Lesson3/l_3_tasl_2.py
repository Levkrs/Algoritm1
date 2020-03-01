#Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в
# этих позициях первого массива стоят четные числа.

import random

SIZE = 14
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
ev_array = []
print(array)

for index, val in enumerate(array):

    # print(f"Индекс = {index} / значение {val}")
    if (val % 2) == 0:
        ev_array.append(index)

print(f"Четные элементы находятся по номера: {ev_array}")
