# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -1000
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

delete_val = []
for i in array:
    if i < 0:
        delete_val.append(i)


min_val = 0
for i in delete_val:
    val = abs(i)
    if min_val <= val:
        min_val = val
min_val_array = array.index((min_val * (-1)))
print(f'Максимальное отрицательное значение позиция {array.index((min_val * (-1)))} | Значение {min_val * -1}')
