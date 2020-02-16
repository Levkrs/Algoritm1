
#Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

#https://drive.google.com/file/d/19cks13sskD9WBvEIaDfd6bpJWkKOjtOo/view?usp=sharing

print("Введите 2 буквы латинского лафавита")

char1 = input("Введите букву 1: ")
char2 = input("Введите бугву 2: ")

#char1 = ord(char1)
#char2 = ord(char2)

pos_char1 = ord(char1) - 96
pos_char2 = int(ord(char2)) - 96

dist = abs(ord(char1) - ord(char2)) - 1


print("Позиция первой буквы: ", pos_char1)
print("Позиция второй буквы ", pos_char2)
print("Колличество бук между 1 и 2 буквой: ", dist)

