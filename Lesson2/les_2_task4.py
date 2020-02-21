# https://drive.google.com/file/d/1YyCABOTbFhWkK235G3cLc8szpnnlYLmH/view?usp=sharing
#4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

print("Введите колличество n элементов")
n = int(input())
a = -0.5
x = 1
i = 0
res = 0

while i != n:
    res = res + (x * a)
    x = x * a
    i += 1

print(res)
