# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).


# https://drive.google.com/file/d/13h4-gCyvOOMlwcgU90Ukgz48NGm4uZCo/view?usp=sharing

print("Введите 3 числа")
a = input("Введите число а: ")
b = input("Введите число b: ")
c = input("Введите число с: ")

if (a > b and a < c):
    print("Среднее: ", a)
elif (b > a and b < c):
    print("Среднее: ", b)
else:
    print("Среднее: ", c)
