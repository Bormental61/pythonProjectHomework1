# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# my_var
# day_num = int(input('Введите номер дня недели: '))
# if day_num == 6 or day_num == 7:
#     print('да')
# else:
#     print('нет')

# alt_var с созданием словаря значений
# day = int(input())
# day_name = {1: 'Понедельник',
#             2: 'Вторник',
#             3: 'Среда',
#             4: 'Четверг',
#             5: 'Пятница',
#             6: 'Суббота',
#             7: 'Воскресенье'}
# print(day_name.get(day, 'Такого дня недели не существует'))

# 7. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# my_var
# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print('Для X =', x,', Y =', y,', Z =', z)
#                 print(not (x or y or z) == (not x and not y and not z))

# alt_var через двоичный код
# for i in range(0b111 + 1):
#     binary_string = format(i, '03b')
#     x = int(binary_string[0])
#     y = int(binary_string[1])
#     z = int(binary_string[2])
#     print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} есть {not (x or y or z) == ((not x) and (not y) and (not z))}')

# 8. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# print('Привет! Эта программа показывает в какой четверти координатной плоскости или на какой оси находится точка с заданными координатами.')
# x = int(input('Введите X: '))
# y = int(input('Введите Y: '))
# while x == 0 and y == 0:
#     x = int(input('X и Y не должны равняться 0 одновременно, так как это точка начала координат, введите X: '))
#     y = int(input('Введите Y: '))
# if x > 0 and y > 0:
#     print('1 четверть')
# elif x < 0 and y > 0:
#     print('2 четверть')
# elif x < 0 and y < 0:
#     print('3 четверть')
# elif x > 0 and y < 0:
#     print('4 четверть')
# elif x == 0:
#     print('Точка на оси X')
# elif y == 0:
#     print('Точка на оси Y')

# 9. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# square_num = int(input('Введите номер четверти: '))
# if square_num == 1:
#     print('x > 0, y > 0')
# elif square_num == 2:
#     print('x < 0, y > 0')
# elif square_num == 3:
#     print('x < 0, y < 0')
# elif square_num == 4:
#     print('x > 0, y < 0')

# 10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# my_var
# x1, y1 = map(float, input('Введите координаты точки 1: ').split(','))
# x2, y2 = map(float, input('Введите координаты точки 2: ').split(','))
# distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# distance *= 100
# distance = int(distance)
# distance = float(distance / 100)
# print('Расстояние между точками =', distance) # (f'Расстояние между точками = {distance:.2f}')

# alt_var с использованием math и разными типами вывода
# import math
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# ac = y2 - y1
# bc = x2 - x1
# print(round((ac ** 2 + bc ** 2) ** 0.5, 2))
# print(int(math.sqrt(ac ** 2 + bc ** 2) * 100) / 100)
# print(str(math.sqrt(ac ** 2 + bc ** 2)).split('.')[0] + '.' + str(math.sqrt(ac ** 2 + bc ** 2)).split('.')[1][:2])
