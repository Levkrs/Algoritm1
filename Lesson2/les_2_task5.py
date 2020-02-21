# https://drive.google.com/file/d/1YyCABOTbFhWkK235G3cLc8szpnnlYLmH/view?usp=sharing

#5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


start_chr = 37
i = 0
res_str = ""

while i != 5:
    j = 0
    while j != 10:
        char_num = start_chr
        char = chr(start_chr)
        j += 1
        start_chr += 1
        res_str = res_str + str(start_chr) + " - " + char + "  | "
    print(res_str)
    res_str = ""
    start_chr = start_chr + 10
    i += 1
