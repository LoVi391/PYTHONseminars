# 1. Напишитье программу, к-я принимает на вход два числа 
# и проверяет, является ли одно число квадратом другого.
# Примеры: 
# -5, 25 -> да




a = int(input('Введите число a -  '))
b = int(input('Введите число b -  '))

if (a == b * b) or (b == a * a):
    print ('да')
else:
    print('нет')

