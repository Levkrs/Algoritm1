# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

cnt_el = [array[0]]

count_end = 1
for i in array:
    count_start = 0
    j = 0
    while j < len(array):
        if i == array[j]:
            count_start += 1
        j += 1
    if count_end <= count_start:
        count_end = count_start
        cnt_el = i
print(f'Чаще всего встречается {cnt_el}')
