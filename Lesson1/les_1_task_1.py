#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

#https://drive.google.com/file/d/19kbY4sRIj-znYIZjNdHTgKlY5_OVSsXP/view?usp=sharing


print("Введите трехзначное целое число: ")
x = int(input())

x1 = abs(x % 10)
x2 = (abs(x % 100) - x1) / 10
x3 = (abs(x % 1000) - abs(x % 100)) / 100
resSumm = x1 + x2 + x3
resSub = (x1 * x2) * x3

print(x1)
print(x2)
print(x3)

print("Результат суммы:", int(resSumm))
print("Результат умножения: ", int(resSub))
