# Определить, является ли год, который ввел пользователь, високосным или не високосным.

#https://drive.google.com/open?id=19cks13sskD9WBvEIaDfd6bpJWkKOjtOo



print("Введите год:")

year = int(input())

if (year%4) == 0:
    print('Год високосный')
else:
    if (year%100) == 0:
        print("Год високосный")
    else:
        if(year%400) == 0:
            print("Год високосный")
        else:print("Год не високосный")