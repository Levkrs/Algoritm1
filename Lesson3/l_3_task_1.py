# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 99
array = []
CRAT_ARRAY = [2, 3, 4, 5, 6, 7, 8, 9]

for i in range(MIN_ITEM, MAX_ITEM + 1):
    array.append(i)

print(array)

for i in CRAT_ARRAY:
    count_crat = 0
    for j in array:
        if (j % i) == 0:
            count_crat += 1
    print(f"Колличество элементов кратных {i} = {count_crat}")
