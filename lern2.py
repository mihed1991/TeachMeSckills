# ЗАДАНИЕ  1 
# # Привести к целому типу -1.6, 2.99

# num1 = - 1.6
# num2 = 2.99
# print(f"num1 = {round(num1)}" ,"\n" f"num2 = {round(num2)}")


# ЗАДАНИЕ 2
# # Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

# str1 = "www.my_site.com#about"
# str1 = str1.replace("#","/")
# print(str1)


# ЗАДАНИЕ 3
# # Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’

# word = "stroka"
# suffix = "ing"
# new_word = "".join([word, suffix])
# print(new_word)

# ЗАДАНИЕ  4
# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

# name = "Doe John"
# first_name, last_name = name.split()
# swapped_name = " ".join([last_name, first_name])
# print(swapped_name)

# ЗАДАНИЕ 5
# Напишите программу которая удаляет пробел в начале, в конце
# строки
# input_string = "  Пример строки с пробелами  "
# output_string = input_string.strip()
# print(f"'{output_string}'")

# ЗАДАНИЕ  6
# Создайте словарь, связав его с переменной school, и наполните его
# данными которые бы отражали количество учащихся в десяти разных
# классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).

# school = {
#     "1а": 25,
#     "1б": 27,
#     "2а": 30,
#     "2б": 28,
#     "3а": 26,
#     "3б": 29,
#     "4а": 24,
#     "4б": 31,
#     "5а": 32,
#     "5б": 30
# }

# print(school)


# ЗАДАНИЕ  7
# Создайте список и извлеките из него списка второй элемент.

# my_list = [10, 20, 30, 40, 50]
# second_element = my_list[1]

# print(second_element)


#  ЗАДАНИЕ 8
# Вывести входит ли строка1 в строку2 (пример: employ и employment )

# string1 = "employ"
# string2 = "employment"
# print(string1 in string2)

# ЗАДАНИЕ 9
# Вывести нужные символы
# x = "My name is Agent Smith"
# print(x[?]) #y
# print(x[?:?:?]) #nesgt

# x = "My name is Agent Smith"

# print(x[1])  # y
 # nesgt ?????


# ЗАДАНИЕ 10
#  Есть массив чисел. Известно, что каждое число в этом массиве имеет
# пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число

# arr = [1, 5, 2, 9, 2, 9, 1]

# unique_number = 0
# for num in arr:
#     unique_number ^= num  # Используем побитовое исключающее ИЛИ (XOR)

# print(unique_number)
