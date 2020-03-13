#Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в
# этих позициях первого массива стоят четные числа.

import random
import timeit
import cProfile

#
# SIZE = 14
# MIN_ITEM = 0
# MAX_ITEM = 100
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# print(array)


def chet_ver1(x):
    ev_array = []
    SIZE = x
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

    for index, val in enumerate(array):

        # print(f"Индекс = {index} / значение {val}")
        if (val % 2) == 0:
            ev_array.append(index)

    #print(f"Четные элементы находятся по номера: {ev_array}")


def chet_ver2(x):
    ev_array2 = []
    SIZE = x
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    i = 0
    while i < len(array):
        if array[i] % 2 == 0:
            ev_array2.append(array.index(array[i]))
            array[i] = -1
        i+=1
    #print(ev_array2)

def chet_ver3(x):
    ev_array3 = []
    SIZE = x
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    array2 = []
    res_array = []
    #print(array)

    for index, val in enumerate(array):
        array2.append(val % 2)
    #print(array2)
    for index, val in enumerate(array2):
        if val == 0:
            res_array.append(array[index])



    #print(res_array)




print("//// ver 1 ")


print(timeit.timeit('chet_ver1(50)', number=100, globals=globals()))     # 0.007348337999999996
print(timeit.timeit('chet_ver1(100)', number=100, globals=globals()))    # 0.016423412
print(timeit.timeit('chet_ver1(200)', number=100, globals=globals()))    # 0.026299585
print(timeit.timeit('chet_ver1(400)', number=100, globals=globals()))    # 0.055800056000000015
print(timeit.timeit('chet_ver1(800)', number=100, globals=globals()))    # 0.11297616099999996

cProfile.run('chet_ver1(50)')
cProfile.run('chet_ver1(100)')
cProfile.run('chet_ver1(150)')
cProfile.run('chet_ver1(200)')
cProfile.run('chet_ver1(400)')
cProfile.run('chet_ver1(800)')


print("//// ver 2 ")

print(timeit.timeit('chet_ver3(50)', number=100, globals=globals()))     # 0.008000434999999972
print(timeit.timeit('chet_ver3(100)', number=100, globals=globals()))    # 0.013947872000000028
print(timeit.timeit('chet_ver3(200)', number=100, globals=globals()))    # 0.027290079999999994
print(timeit.timeit('chet_ver3(400)', number=100, globals=globals()))    # 0.05512988600000002
print(timeit.timeit('chet_ver3(800)', number=100, globals=globals()))    # 0.12674956800000003

cProfile.run('chet_ver1(50)')
cProfile.run('chet_ver1(100)')
cProfile.run('chet_ver1(150)')
cProfile.run('chet_ver1(200)')
cProfile.run('chet_ver1(400)')
cProfile.run('chet_ver1(800)')


print("//// ver 3 ")


print(timeit.timeit('chet_ver2(50)', number=100, globals=globals()))     # 0.008727251000000047
print(timeit.timeit('chet_ver2(100)', number=100, globals=globals()))    # 0.024314983000000012
print(timeit.timeit('chet_ver2(200)', number=100, globals=globals()))    # 0.05111335799999994
print(timeit.timeit('chet_ver2(400)', number=100, globals=globals()))    # 0.12923470700000006
print(timeit.timeit('chet_ver2(800)', number=100, globals=globals()))    # 0.3865415139999999

cProfile.run('chet_ver1(50)')
cProfile.run('chet_ver1(100)')
cProfile.run('chet_ver1(150)')
cProfile.run('chet_ver1(200)')
cProfile.run('chet_ver1(400)')
cProfile.run('chet_ver1(800)')


print("////// ")


# Судя по timeit самый тяжелый алгоритм ver 3, так как был выдуман для самого большоего колличества дейстий.