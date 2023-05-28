# Задача 1.1.

# Есть строка с перечислением песен

# my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

List_songs = len(my_favorite_songs)
print(my_favorite_songs[0:14])
print(my_favorite_songs[-13:])
print(my_favorite_songs[16:30])
print(my_favorite_songs[-26:-15])

 
# Задача 1.2.
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random
three_songs = random.sample(my_favorite_songs, 3)
time = round(three_songs[0][1]+ three_songs[1][1] + three_songs[2][1])
print("Три песни звучат:", time, "минут")



# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

import random
times = random.sample(list(my_favorite_songs_dict.values()), 3)
times_three_songs = round(sum(times))
print("Три песни звучат", times_three_songs, "минут")


# Задача 1.3
# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом
month = int(input('Введите, пожалуйста, номер месяца: '))
if month == 1:
    print('Вы ввели январь. 31 дней')
elif month == 2:
    print('Вы ввели февраль. 28 дней')
elif month == 3:
    print('Вы ввели март. 31 дней')
elif month == 4:
    print('Вы ввели апрель. 30 дней')
elif month == 5:
    print('Вы ввели май. 31 дней')
elif month == 6:
    print('Вы ввели июнь. 30 дней')
elif month == 7:
    print('Вы ввели июль. 31 дней')
elif month == 8:
    print('Вы ввели август. 31 дней')
elif month == 9:
    print('Вы ввели сентябрь. 30 дней')
elif month == 10:
    print('Вы ввели октябрь. 31 дней')
elif month == 11:
    print('Вы ввели ноябрь. 30 дней')
elif month == 12:
    print('Вы ввели декабрь. 31 дней')
else:
    print('Такого месяца нет!')



# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

for name_titles in titles:
    code_titles = titles[name_titles]
    total_price = 0
    total_quantity = 0
    for quantity_price in store[code_titles]:
        total_price = total_price + quantity_price['quantity'] * quantity_price['price']
        total_quantity += quantity_price['quantity']
    print(name_titles, '-', total_quantity, 'шт, стоимость', total_price, 'руб')



# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!


def maximum(arr):
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
            max_ = ele
    return max_ 
def minimum(arr):
    min_=arr[0]
    for ele in arr:
        if ele < min_:
           min_ = ele
    return min_
list1 = [69, 59, 2, 43, -12, 18]
result = maximum(list1)
result1 = minimum(list1)
print("max =", result, "min =", result1)


# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    if month == 1: 
        print("Месяц 1 (январь) является частью первого квартала")
    elif month == 2:
        print("Месяц 2 (февраль) является частью первого квартала")
    elif month == 3:
        print("Месяц 3 (март) является частью первого квартала")
    elif month == 4:
        print("Месяц 4 (апрель) является частью второго квартала")
    elif month == 5:
        print("Месяц 5 (май) является частью второго квартала")
    elif month == 6:
        print("Месяц 6 (июнь) является частью второго квартала")
    elif month == 7:
        print("Месяц 7 (июль) является частью третьего квартала")
    elif month == 8:
        print("Месяц 8 (август) является частью третьего квартала")
    elif month == 9:
        print("Месяц 9 (сентябрь) является частью третьего квартала")
    elif month == 10:
        print("Месяц 10 (октябрь) является частью четвертого квартала")
    elif month == 11:
        print("Месяц 11 (ноябрь) является частью четвертого квартала")
    elif month == 12:
        print("Месяц 12 (декабрь) является частью четвертого квартала")
    else:
        print("Такого месяца нет")
quarter_of(4)



# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

n = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
def switch_it_up(number):
    for key, value in n.items():
        while number == key:
            return value
    return "None"
print(switch_it_up(8))


# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"


def remove_exclamation_marks(s):
    return s.replace("!", "")
print(remove_exclamation_marks("Hi! Hello!"))
print(remove_exclamation_marks(" "))
print(remove_exclamation_marks("Oh, no!!!"))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"


def remove_last_em(s):
    i=0
    while i < 1 and s[-1]=="!":
        s = s[:-1]
        i+=1
    else: 
        pass
        return s
print(remove_last_em("Hi!"))
print(remove_last_em("Hi!!!"))
print(remove_last_em("!Hi"))

# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

n = int(input("Введите количество строк: "))
m = int(input("Введите количество колонок: "))
x = int(input("Введите число: "))
list = []
for row in range(n):
    inner_list = []
    for col in range(m):
        inner_list.append(x)
    list.append(inner_list)
for Matrix in list:
    print(str(Matrix)+"\n")
  
  
# Задача 4.1.

import sqlite3
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
sqlquery = """CREATE TABLE Students 
(Student_Id Int NOT NULL, 
 Student_Name Text NOT NULL, 
 School_Id Int NOT NULL Primary key);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

import sqlite3
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
sqlquery = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
VALUES 
(201, 'Иван', 1), 
(202, 'Петр', 2), 
(203, 'Анастасия', 3), 
(204, 'Игорь', 4);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

import sqlite3
def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection
def close_connection(connection):
    if connection:
        connection.close()

def get_student_data(Student_Id):
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = '''SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name 
    FROM Students 
    JOIN School ON Students.School_Id = School.School_Id;'''
    cursor.execute(sqlquery)
    result = cursor.fetchall()
    print ("Данные по студенту")
    for row in result:
        print ("ID студента: ", row[0])
        print ("Имя студента: ", row[1])
        print ("ID школы: ", row[2])
        print ("Название школы: ", row[3])
    connection.close()
get_student_data(201)
