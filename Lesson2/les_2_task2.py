# https://drive.google.com/file/d/1YyCABOTbFhWkK235G3cLc8szpnnlYLmH/view?usp=sharing

#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

print("Введите натуральное число")

a = int(input())
#a = 3452233
print(a)

cnt = len(str(a))

i = 0
chet = ""
nechet = ""
count_chet = 0
count_nechet = 0

while i != cnt:
    b = int(a % 10)
    a = a // 10
    if (b % 2) == 0:
        chet = chet + str(b) + ","
        count_chet += 1
        i += 1
    else:
        nechet = nechet + str(b) + ","
        count_nechet += 1
        i += 1
print(
    f"Колличество четных чисел: {count_chet} - числа {chet}.  Колличество нечетных чисел: {count_nechet} - числа {nechet}")
