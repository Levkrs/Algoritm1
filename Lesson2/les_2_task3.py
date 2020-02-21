# https://drive.google.com/file/d/1YyCABOTbFhWkK235G3cLc8szpnnlYLmH/view?usp=sharing


#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


print("Введите число")

a = int(input())

res = ""


def recu(a, res):
    if (a == 0):
        return res
    else:
        res = res + str(int(a % 10))
        a = int((a - (a % 10)) / 10)
        return recu(a, res)


z = recu(a, res)
print(z)
