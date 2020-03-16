"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

comp_count = int(input("Какое колличство предприятий будете вводить? "))

firm = []

new_firm = namedtuple('new_firm', 'name_firm kv1 kv2 kv3 kv4')

i = 1
while i <= comp_count:
    nameFirm = input("Введите название фирмы: ")
    kv1_f = input("Введите прибыль за 1 квартал ")
    kv2_f = input("Введите прибыль за 2 квартал ")
    kv3_f = input("Введите прибыль за 3 квартал ")
    kv4_f = input("Введите прибыль за 4 квартал ")
    firm.append(new_firm(nameFirm, kv1_f, kv2_f, kv3_f, kv4_f))
    i += 1


# print(firm)


def sr_prib(firm):
    sr_prib_mass = []
    high_prib = []
    low_prib = []
    sr_pr = 0
    for j, val in enumerate(firm):
        res = int(val.kv1) + int(val.kv2) + int(val.kv3) + int(val.kv4)
        sr_pr = sr_pr + res
        sr_prib_mass.append([firm[j].name_firm, res / 4])
        # print(res)
    #print(sr_pr / 8)
    #print(sr_prib_mass)
    for j, val in enumerate(sr_prib_mass):
        if val[1] >= sr_pr / 8:
            high_prib.append(val[0])
        else:
            low_prib.append(val[0])
    print("Прибыль выше средрей: ", high_prib, sep="\n")
    print("Прибыль ниже средней: ", low_prib, sep="\n")


sr_prib(firm)
